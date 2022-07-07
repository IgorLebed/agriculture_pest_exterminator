#!/usr/bin/env python3

# THE SKELETON OF THE MAIN PROGRAM

import rospy
import json
from numpy import nan, isnan
from sensor_msgs.msg import NavSatFix
import gnss_math as gm
from class1 import FourXFourBotControl

# =====
# ANGLE
# =====
latitude = None
longitude = None


def nav_cb(nsf):
    latitude = nsf.latitude
    longitude = nsf.longitude


rospy.init_node('tx2', anonymous=True)
nav = rospy.Subscriber('fix', NavSatFix, nav_cb, queue_size=10)

# ==============
# GETTING POINTS
# ==============
with open('trajectory.json') as file:
    point_list = json.load(file)
rospy.loginfo(f'Trajectory loaded, number of points: {len(point_list)}')

# ================
# PASSING BY POINT
# ================
err_dist = 1  # m, allowable error TODO: choose the best
err_angl = 20  # degrees, allowable error TODO: choose the best
latitude_old = latitude
longitude_old = longitude

ffbc = FourXFourBotControl()
rospy.loginfo('Wheel control loaded')


for point in point_list:
    rospy.loginfo(f'Point: {point}')
    while not rospy.is_shutdown():
        ffbc.set_wheels_frequency(0, 0)
        rospy.loginfo('-- 0  0')
        if latitude is not None and longitude is not None:
            dist = gm.distance((latitude, longitude), (point[0], point[1]))
            rospy.loginfo(f'dist: {dist}')
            # TODO:  photo
            # Distance
            if dist > err_dist:
                angl = gm.angle((latitude_old, longitude_old),
                                (latitude, longitude), (point[0], point[1]))
                rospy.loginfo(f'angl: {angl}')
                ffbc.set_wheels_frequency(20, 20)
                rospy.loginfo('-- 20 20')
                rospy.sleep(5)
                # Angle
                if abs(angl) > err_angl:
                    if abs(angl) < 60:
                        angl_wheel = 30
                    elif abs(angl) < 120:
                        angl_wheel = 45
                    elif abs(angl) <= 180:
                        angl_wheel = 60
                    if angl > 0:
                        ffbc.set_wheels_frequency(angl_wheel, 0)
                        rospy.loginfo(f'-- {angl_wheel} 0')
                    else:
                        ffbc.set_wheels_frequency(0, angl_wheel)
                        rospy.loginfo(f'-- 0  {angl_wheel}')
                rospy.sleep(5)
                latitude_old = latitude
                longitude_old = longitude
            else:
                break
        else:
            rospy.sleep(1)
ffbc.set_wheels_frequency(0, 0)
rospy.loginfo('-- 0  0')
