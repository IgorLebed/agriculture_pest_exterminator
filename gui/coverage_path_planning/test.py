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


def main():
	sweep_resolution = 5
	flight_area_vertices = np.array([[-10, -10], [-10, 10], [10, 10], [10, -10]])
	
	ox = flight_area_vertices[:,0].tolist() + [flight_area_vertices[0,0]]
	oy = flight_area_vertices[:,1].tolist() + [flight_area_vertices[0,1]]
	print("Ox:", ox)
	print("Oy:", oy)
	print("sweep:", sweep_resolution)
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