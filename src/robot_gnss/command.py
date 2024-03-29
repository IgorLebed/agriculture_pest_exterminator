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
    left_front = speed.data


def lb_cb(speed):
    global left_back
    left_back = speed.data


def rf_cb(speed):
    global right_front
    right_front = speed.data


def rb_cb(speed):
    global right_back
    right_back = speed.data


def set_speed(left, right, last_left, last_right):
    ffbc.set_wheels_frequency(left, right)
    if (abs(left - last_left) < 10 and abs(right - last_right) < 10):
        for i in range(10):
            ffbc.set_wheels_frequency(left, right)
            rospy.sleep(0.2)
    elif abs(left - last_left) < 10:
        while (abs(right_front - last_right) < 6
               or abs(right_back - last_right) < 6):
            ffbc.set_wheels_frequency(left, right)
            rospy.sleep(0.2)
    elif abs(right - last_right) < 10:
        while (abs(left_front - last_left) < 6
               or abs(left_back - last_left) < 6):
            ffbc.set_wheels_frequency(left, right)
            rospy.sleep(0.2)
    else:
        while (abs(left_front - last_left) < 6
               or abs(left_back - last_left) < 6
               or abs(right_front - last_right) < 6
               or abs(right_back - last_right) < 6):
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

        set_speed(left, right, 0, 0)
        # ffbc.set_wheels_frequency(left, right)
        rospy.sleep(time)

        set_speed(0, 0, left, right)
        # ffbc.set_wheels_frequency(0, 0)
