"""
Coverage path planning (CPP) algorithm implementation for a mobile robot
equipped with 4 ranger sensors (front, back, left and right)
for obstacles detection.

"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import math
from grid_map import GridMap
from grid_based_sweep_coverage_path_planner import planning
import time
from tools import define_polygon, polygon_contains_point

"""def plot_robot(pose, params):
	r = params.sensor_range_m
	plt.plot([pose[0]-r*np.cos(pose[2]), pose[0]+r*np.cos(pose[2])],
			 [pose[1]-r*np.sin(pose[2]), pose[1]+r*np.sin(pose[2])], '--', color='b')
	plt.plot([pose[0]-r*np.cos(pose[2]+np.pi/2), pose[0]+r*np.cos(pose[2]+np.pi/2)],
		     [pose[1]-r*np.sin(pose[2]+np.pi/2), pose[1]+r*np.sin(pose[2]+np.pi/2)], '--', color='b')
	plt.plot(pose[0], pose[1], 'ro', markersize=5)
	plt.arrow(pose[0], pose[1], 0.05 * np.cos(pose[2]), 0.05 * np.sin(pose[2]),
              head_length=0.1, head_width=0.1)"""

def obstacle_check(pose, gridmap, params):
	gmap = gridmap

	r = int(100*params.sensor_range_m)
	back = [pose[0]-r*np.cos(pose[2]), pose[1]-r*np.sin(pose[2])]
	front = [pose[0]+r*np.cos(pose[2]), pose[1]+r*np.sin(pose[2])]
	right = [pose[0]+r*np.cos(pose[2]+np.pi/2), pose[1]+r*np.sin(pose[2]+np.pi/2)]
	left = [pose[0]-r*np.cos(pose[2]+np.pi/2), pose[1]-r*np.sin(pose[2]+np.pi/2)]

	pi = np.array(pose[:2], dtype=int)
	backi = np.array(back, dtype=int)
	fronti = np.array(front, dtype=int)
	lefti = np.array(left, dtype=int)
	righti = np.array(right, dtype=int)

	obstacle = {
		'front': 0,
		'back':  0,
		'right': 0,
		'left':  0,
	}

	for i in np.arange(min(pi[0], fronti[0]), max(pi[0], fronti[0])+1):
		for j in np.arange(min(pi[1], fronti[1]), max(pi[1], fronti[1])+1):
			m = min(j, gmap.shape[0]-1); n = min(i, gmap.shape[1]-1)
			if gmap[m,n]:
				# print('FRONT collision')
				obstacle['front'] = 1

	for i in np.arange(min(pi[0], backi[0]), max(pi[0], backi[0])+1):
		for j in np.arange(min(pi[1], backi[1]), max(pi[1], backi[1])+1):
			m = min(j, gmap.shape[0]-1); n = min(i, gmap.shape[1]-1)
			if gmap[m,n]:
				# print('BACK collision')
				obstacle['back'] = 1

	for i in np.arange(min(pi[0], lefti[0]), max(pi[0], lefti[0])+1):
		for j in np.arange(min(pi[1], lefti[1]), max(pi[1], lefti[1])+1):
			m = min(j, gmap.shape[0]-1); n = min(i, gmap.shape[1]-1)
			if gmap[m,n]:
				# print('LEFT collision')
				obstacle['left'] = 1

	for i in np.arange(min(pi[0], righti[0]), max(pi[0], righti[0])+1):
		for j in np.arange(min(pi[1], righti[1]), max(pi[1], righti[1])+1):
			m = min(j, gmap.shape[0]-1); n = min(i, gmap.shape[1]-1)
			if gmap[m,n]:
				# print('RIGHT collision')
				obstacle['right'] = 1

	return obstacle



def left_shift(pose, r):
	left = [pose[0]+r*np.cos(pose[2]+np.pi/2), pose[1]+r*np.sin(pose[2]+np.pi/2)]
	return left
def right_shift(pose, r):
	right = [pose[0]-r*np.cos(pose[2]+np.pi/2), pose[1]-r*np.sin(pose[2]+np.pi/2)]
	return right
def back_shift(pose, r):
	back = pose
	back[:2] = [pose[0]-r*np.cos(pose[2]), pose[1]-r*np.sin(pose[2])]
	return back
def forward_shift(pose, r):
	forward = pose
	forward[:2] = [pose[0]+r*np.cos(pose[2]), pose[1]+r*np.sin(pose[2])]
	return forward
def turn_left(pose, yaw=np.pi/2*np.random.uniform(0.2, 0.6)):
	pose[2] -= yaw
	return pose
def turn_right(pose, yaw=np.pi/2*np.random.uniform(0.2, 0.6)):
	pose[2] += yaw
	return pose
def slow_down(state, params, dv=0.1):
	if state[3]>params.min_vel:
		state[3] -= dv
	return state

"""def visualize(traj, pose, params):
	plt.plot(traj[:,0], traj[:,1], 'g')
	plot_robot(pose, params)
	plt.legend()"""
		

def motion(state, goal, params):
	# state = [x(m), y(m), yaw(rad), v(m/s), omega(rad/s)]
	dx = goal[0] - state[0]
	dy = goal[1] - state[1]
	goal_yaw = math.atan2(dy, dx)
	K_theta = 3
	state[4] = K_theta*math.sin(goal_yaw - state[2]) # omega(rad/s)
	state[2] += params.dt*state[4] # yaw(rad)

	dist_to_goal = np.linalg.norm(goal - state[:2])
	K_v = 0.1
	state[3] += K_v*dist_to_goal
	if state[3] >= params.max_vel: state[3] = params.max_vel
	if state[3] <= params.min_vel: state[3] = params.min_vel

	dv = params.dt*state[3]
	state[0] += dv*np.cos(state[2]) # x(m)
	state[1] += dv*np.sin(state[2]) # y(m)

	return state

def collision_avoidance(state, gridmap, params):
	pose_grid = gridmap.meters2grid(state[:2])
	boundary = obstacle_check([pose_grid[0], pose_grid[1], state[2]], gridmap.gmap, params)
	# print(boundary)

	if boundary['right'] or boundary['front']:
		# state = back_shift(state, 0.03)
		state = slow_down(state, params)
		state = turn_left(state, np.radians(30))
		# state = forward_shift(state, 0.02)
	elif boundary['left']:
		# state = back_shift(state, 0.03)
		state = slow_down(state, params)
		state = turn_right(state, np.radians(30))
		# state = forward_shift(state, 0.02)
	return state

'''def define_flight_area(initial_pose):
	plt.grid()
	while True:
		try:
			num_pts = int( input('Enter number of polygonal vertixes: ') )
			break
		except:
			print('\nPlease, enter an integer number.')
	while True:
		flight_area_vertices = define_polygon(num_pts)
		if polygon_contains_point(initial_pose, flight_area_vertices):
			break
		plt.clf()
		plt.grid()
		print('The robot is not inside the flight area. Define again.')
	return flight_area_vertices'''

class Params:
	def __init__(self):
		self.numiters = 1000
		#self.animate = 0
		self.dt = 0.1
		self.goal_tol = 0.15
		self.max_vel = 0.5 # m/s
		self.min_vel = 0.1 # m/s
		self.sensor_range_m = 0.3 # m
		self.time_to_switch_goal = 5.0 # sec
		#self.sweep_resolution = 0.1 # m

def main():
	obstacles = [
		#np.array([[0.7, -0.9], [1.3, -0.9], [1.3, -0.8], [0.7, -0.8]]) + np.array([-1.0, 0.5]),
		#np.array([[0.7, -0.9], [1.3, -0.9], [1.3, -0.8], [0.7, -0.8]]) + np.array([-1.0, 1.0]),
		#np.array([[0.7, -0.9], [0.8, -0.9], [0.8, -0.3], [0.7, -0.3]]) + np.array([-1.5, 1.0]),        
	
		#np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]])*0.5
	]
	sweep_resolution = input("Input resolution: ")
	# initial state = [x(m), y(m), yaw(rad), v(m/s), omega(rad/s)]
	state = np.array([0, 0.2, np.pi/2, 0.0, 0.0])
	traj = state[:2]
	params = Params()
	#plt.figure(figsize=(10,10))
	#flight_area_vertices = define_flight_area(state[:2])
	flight_area_vertices = np.array([[-10, -10], [-10, 10], [10, 10], [10, -10]])
	gridmap = GridMap(flight_area_vertices, state[:2])
	#gridmap.add_obstacles_to_grid_map(obstacles)
	
	ox = flight_area_vertices[:,0].tolist() + [flight_area_vertices[0,0]]
	oy = flight_area_vertices[:,1].tolist() + [flight_area_vertices[0,1]]
	#reso = params.sweep_resolution
	#reso = 0.4
	print(ox)
	goal_x, goal_y = planning(ox, oy, sweep_resolution)
	# goal = [x, y], m
	goali = 0
	goal = [goal_x[goali], goal_y[goali]]
	t_prev_goal = time.time()

	# gridmap.draw_map(obstacles)

	# while True:
	'''for _ in range(params.numiters):
		state = motion(state, goal, params)

		state = collision_avoidance(state, gridmap, params)

		goal_dist = np.linalg.norm(goal - state[:2])
		
		t_current = time.time()
		#traj = np.vstack([traj, state[:2]])'''
		
	print('Mission is complete!')
	#plt.plot(goal_x, goal_y)
	
	#visualize(traj, state, params)
	#plt.show()

if __name__ == '__main__':
	main()
	'''try:
		main()
	except KeyboardInterrupt:
	    pass'''
		
