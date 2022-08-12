#!/usr/bin/env python3

from rosclass1 import FourXFourBotControl
import rospy

rospy.init_node('tx2', anonymous=True)
ffbc = FourXFourBotControl()

while not rospy.is_shutdown():
    left = int(input(' left: '))
    if left > 120:
        break
    right = int(input('right: '))
    time = float(input('time: '))

    for i in range(5):
        ffbc.set_wheels_frequency(left, right)
        # rospy.sleep(0.1)
    rospy.sleep(time)

    for i in range(5):
        ffbc.set_wheels_frequency(0, 0)
        # rospy.sleep(0.1)
