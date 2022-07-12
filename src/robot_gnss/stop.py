#!/usr/bin/env python3

from class1 import FourXFourBotControl
import rospy

rospy.init_node('tx2', anonymous=True)
ffbc = FourXFourBotControl()

for i in range(10):
    ffbc.set_wheels_frequency(0, 0)
    rospy.sleep(0.5)
