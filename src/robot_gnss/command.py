#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int8
from rosclass1 import FourXFourBotControl

# ===============
# Wheels callback
# ===============
left_front = 0
left_back = 0
right_front = 0
right_back = 0


def lf_cb(speed):
    global left_front
    left_front = speed


def lb_cb(speed):
    global left_back
    left_back = speed


def rf_cb(speed):
    global right_front
    right_front = speed


def rb_cb(speed):
    global right_back
    right_back = speed


def set_speed(time, left, right, last_left, last_right):
    ffbc.set_wheels_frequency(left, right)
    while (abs(left_front - last_left) < 5
           or abs(left_back - last_left) < 5
           or abs(right_front - last_right) < 5
           or abs(right_back - last_right) < 5):
        ffbc.set_wheels_frequency(left, right)
        rospy.sleep(0.2)


if __name__ == '__main__':
    lf_sub = rospy.Subscriber('/rpm_left_front', Int8, lf_cb, queue_size=10)
    lb_sub = rospy.Subscriber('/rpm_left_back', Int8, lb_cb, queue_size=10)
    rf_sub = rospy.Subscriber('/rpm_right_front', Int8, rf_cb, queue_size=10)
    rb_sub = rospy.Subscriber('/rpm_right_back', Int8, rb_cb, queue_size=10)

    rospy.init_node('tx2', anonymous=True)
    ffbc = FourXFourBotControl()

    while not rospy.is_shutdown():
        left = int(input(' left: '))
        if left > 120:
            break
        right = int(input('right: '))
        time = float(input('time: '))

        set_speed(time, left, right, 0, 0)
        # ffbc.set_wheels_frequency(left, right)
        rospy.sleep(time)

        set_speed(0, 0, 0, left, right)
        # ffbc.set_wheels_frequency(0, 0)
