#!/usr/bin/env python3

# Тест получения данных с GNSS модуля
# Скрипт копит значения и выдает среднее арифметическое

import rospy
from numpy import isnan, mean
from sensor_msgs.msg import NavSatFix

list_size = 300
count = 0
list_latitude = [0] * list_size
list_longitude = [0] * list_size


def nav_cb(nsf):
    global count
    print(count)
    if count < list_size and not isnan(nsf.latitude):
        print(f'{nsf.latitude}    {nsf.longitude}')
        list_latitude[count] = nsf.latitude
        list_longitude[count] = nsf.longitude
        count += 1
    else:
        print('-')


rospy.init_node('test_gnss', anonymous=True)
nav = rospy.Subscriber('fix', NavSatFix, nav_cb, queue_size=10)

while count < list_size and not rospy.is_shutdown():
    rospy.sleep(0.5)

latitude = mean(list_latitude)
longitude = mean(list_longitude)
print('\nRESULT')
print(f'latitude: {latitude}')
print(f'longitude: {longitude}')
