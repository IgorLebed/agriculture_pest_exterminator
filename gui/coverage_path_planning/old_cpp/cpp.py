"""
Coverage path planning (CPP) algorithm implementation for a mobile robot
equipped with 4 ranger sensors (front, back, left and right)
for obstacles detection.

"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from grid_map import GridMap
from grid_based_sweep_coverage_path_planner import planning
from tools import define_polygon, polygon_contains_point
import pyproj
import scipy.spatial.transform 

#TODO: TEST TRANS FROM GPS 

def from_gps_to_local(lat, lon, alt, lat_org, lon_org, alt_org):
	transformer = pyproj.Transformer.from_crs(
        {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},
        {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'},
        )
	x, y, z = transformer.transform( lon,lat,  alt,radians=False)
	x_org, y_org, z_org = transformer.transform( lon_org,lat_org,  alt_org,radians=False)
	vec=np.array([[ x-x_org, y-y_org, z-z_org]]).T
	rot1 =  scipy.spatial.transform.Rotation.from_euler('x', -(90-lat_org), degrees=True).as_matrix()#angle*-1 : left handed *-1
	rot3 =  scipy.spatial.transform.Rotation.from_euler('z', -(90+lon_org), degrees=True).as_matrix()#angle*-1 : left handed *-1
	rotMatrix = rot1.dot(rot3)    
	enu = rotMatrix.dot(vec).T.ravel()
	return enu.T


def from_local_to_gps(x,y,z, lat_org, lon_org, alt_org):
	transformer1 = pyproj.Transformer.from_crs(
        {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},
        {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'},
        )
	transformer2 = pyproj.Transformer.from_crs(
        {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'},
        {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},
        )
	x_org, y_org, z_org = transformer1.transform( lon_org,lat_org,  alt_org,radians=False)
	ecef_org=np.array([[x_org,y_org,z_org]]).T
	rot1 =  scipy.spatial.transform.Rotation.from_euler('x', -(90-lat_org), degrees=True).as_matrix()#angle*-1 : left handed *-1
	rot3 =  scipy.spatial.transform.Rotation.from_euler('z', -(90+lon_org), degrees=True).as_matrix()#angle*-1 : left handed *-1
	rotMatrix = rot1.dot(rot3)
	ecefDelta = rotMatrix.T.dot( np.array([[x,y,z]]).T )
	ecef = ecefDelta+ecef_org
	lon, lat, alt = transformer2.transform( ecef[0,0],ecef[1,0],ecef[2,0],radians=False)
	return [lat,lon,alt]

#TODO: READING MISSION FILE
'''def define_flight_area(initial_pose):
	f = open('mission.json')
	data = json.load(f)
	for i in data['emp_details']:
    	print(i)
	f.close()
	return flight_area_vertices'''

def main():
	sweep_resolution = input("Input resolution: ")
	flight_area_vertices = np.array([[-10, -10], [-10, 10], [10, 10], [10, -10]])

	# The local coordinate origin (EXAMPLE Zermatt, Switzerland)
	lat_org = 46.017 # deg
	lon_org = 7.750  # deg
	alt_org   = 1673     # meters

    # The point of interest
	lat = 45.976  # deg
	lon = 7.658   # deg
	alt = 4531      # meters

	res1 = from_gps_to_local(lat, lon, alt, lat_org, lon_org, alt_org)
	#print (res1)
    #[-7134.75719598 -4556.32151385  2852.39042395]
    
	x=res1[0]
	y=res1[1]
	z=res1[2]
	res2 = from_local_to_gps(x,y,z, lat_org, lon_org, alt_org)
	#print (res2)
    #[45.97600000000164, 7.658000000000001, 4531.0000001890585]
	
	ox = flight_area_vertices[:,0].tolist() + [flight_area_vertices[0,0]]
	oy = flight_area_vertices[:,1].tolist() + [flight_area_vertices[0,1]]
	goal_x, goal_y = planning(ox, oy, sweep_resolution)
	cpp_path = []
	for a, b in zip( goal_x, goal_y ):
		cpp_path.append( [ a, b ] )
	print('path points')
	print(cpp_path)
	#plt.plot(goal_x, goal_y)
	#plt.show()

if __name__ == '__main__':
	main()