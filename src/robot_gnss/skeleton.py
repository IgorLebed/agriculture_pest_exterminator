#!/usr/bin/env python3

# THE SKELETON OF THE MAIN PROGRAM

import rospy
from numpy import nan, isnan
from sensor_msgs.msg import NavSatFix
import gnss_math as gm

# =====
# ANGLE
# =====
latitude = 1
longitude = 1


def nav_cb(nsf):
    latitude = nsf.latitude
    longitude = nsf.longitude


rospy.init_node('robot', anonymous=True)
nav = rospy.Subscriber('fix', NavSatFix, nav_cb, queue_size=10)

# ==============
# GETTING POINTS
# ==============
# TODO: GET POINTS
point_list = [[100, 100][110, 110][120, 120][130, 130]]  # загруженные точки

# ================
# PASSING BY POINT
# ================
err_dist = 1  # m, allowable error
err_angl = 15  # degrees, allowable error
latitude_old = latitude
longitude_old = longitude

for point in point_list:
    while gm.distance((latitude, longitude), (point)) > err_dist:  # Until we reach the point
        dist = gm.distance((latitude, longitude), (point))
        angl = gm.angle((latitude_old, longitude_old),
                        (latitude, longitude),
                        (point))
        # Updating *_old must be done at the beginning of the iteration,
        # but after all the calculations where *_old is needed
        latitude_old = latitude
        longitude_old = longitude
        if abs(angl) > err_angl:
            # TODO: TURN
            pass
        # TODO: GO AHEAD
        # TODO: SLEEP(1)
