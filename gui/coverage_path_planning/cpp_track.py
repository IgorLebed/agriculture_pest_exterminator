"""
Performs GEOJSON mission file reading, GPS-coordinates conversion to ENU system,
CPP trajectory calculation, waypoints conversion back to GPS-coordinates,
trajectory JSON file generation.

"""
import os
from pathlib import Path
import json
import geojson
import pymap3d as pm
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from grid_map import GridMap
from grid_based_sweep_coverage_path_planner import planning
#from tools import define_polygon, polygon_contains_point


"""
#generate JSON data
data = {
	"polygon":[
		{ "latitude": 59.949379, "longitude": 30.618275 },
		{ "latitude": 59.949434, "longitude": 30.618637 },
		{ "latitude": 59.949301, "longitude": 30.618758 },
		{ "latitude": 59.949262, "longitude": 30.618321 }
	],
	"central_point":[
		{ "latitude": 59.949345, "longitude": 30.618524 }
	]
}
json_string = json.dumps(data,sort_keys=True, indent=4)

# save JSON data
with open("mission.json", "w") as outfile:
	outfile.write(json_string)
"""

def export_polygon(filename):
	mission_data = []
	lat = []
	lon = []
	if os.path.exists(filename):
		with open(filename, "r") as f: 
			mission_data = geojson.load(f) 
			if type(mission_data['features'][0]['geometry']) == geojson.geometry.Polygon:
				my_polygon = mission_data['features'][0]['geometry']['coordinates']
				for i in range(len(my_polygon[0])):
					lat.append(my_polygon[0][i][1])
					lon.append(my_polygon[0][i][0])
				lat.pop(0)
				lon.pop(0)
			if type(mission_data['features'][1]['geometry']) == geojson.geometry.Polygon:
				my_polygon = mission_data['features'][1]['geometry']['coordinates']
				print(my_polygon[0])
				for i in range(len(my_polygon[0])):
					lat.append(my_polygon[0][i][1])
					lon.append(my_polygon[0][i][0])
				lat.pop(0)
				lon.pop(0)
			else:
				print("No polygon!")
	else:
		print("There is no file with mission!")
	print("poly" , lat ,lon)
	return lat, lon


def export_central_point(filename):
	point_data = []
	if os.path.exists(filename):
		with open(filename, "r") as f: 
			point_data = geojson.load(f) 
			if type(point_data['features'][0]['geometry']) == geojson.geometry.Point:
				my_point = point_data['features'][0]['geometry']['coordinates']
				lat0 = my_point[1]
				lon0 = my_point[0]
			if type(point_data['features'][1]['geometry']) == geojson.geometry.Point:
				my_point = point_data['features'][1]['geometry']['coordinates']
				lat0 = my_point[1]
				lon0 = my_point[0]
			else:
				print("No central point!")
	else:
		print("There is no file with mission!")
	print("CP", lat0, lon0)
	return float(lat0), float(lon0)
	

def main():

	enu_coord =    []
	x_enu_coord =  []
	y_enu_coord =  []
	poly_mission_= []
	cpp_path =     []
	cpp_path_gps = []
	h0_ = 0 
	h_ = 0   

	sweep_resolution = 10 #TODO: dynamic import through GUI

	home = str(Path.home())
	path = home + '/agriculture_pest_exterminator/gui/coverage_path_planning/mission.geojson'
	lat0_, lon0_ = export_central_point(path)		# to change filename/path to file
	lat_, lon_ = export_polygon(path)				# to change filename/path to file
	
	for i in range(len(lat_)):
		enu_coord.append(pm.geodetic2enu(lat_[i], lon_[i], h_, lat0_, lon0_, h0_))
	
	for i in range(len(enu_coord)):
		x_enu_coord.append(enu_coord[i][0])
		y_enu_coord.append(enu_coord[i][1])

	poly_mission = list(zip(x_enu_coord, y_enu_coord))

	for i in range(len(x_enu_coord)):
		poly_mission_.append(list(poly_mission[i]))
	
	flight_area_vertices = np.array(poly_mission_)
	ox = flight_area_vertices[:,0].tolist() + [flight_area_vertices[0,0]]
	oy = flight_area_vertices[:,1].tolist() + [flight_area_vertices[0,1]]
	goal_x, goal_y = planning(ox, oy, sweep_resolution)
	
	for a, b in zip(goal_x, goal_y):
		cpp_path.append([a, b])

	for i in range(len(cpp_path)):
		cpp_path_gps.append(pm.enu2geodetic(goal_x[i], goal_y[i], h_, lat0_, lon0_, h0_))

	json_string = json.dumps(list(cpp_path_gps))
	path_out = home + '/agriculture_pest_exterminator/gui/coverage_path_planning/'
	with open(path_out + "trajectory.json", "w") as outfile:
		outfile.write(json_string)
	
	print('Waypoints(ENU):')
	print(cpp_path)
	plt.plot(goal_x, goal_y)
	x_enu_coord.append(x_enu_coord[0])
	y_enu_coord.append(y_enu_coord[0])
	plt.plot(x_enu_coord, y_enu_coord)
	plt.show()
	
if __name__ == '__main__':
	main()