#!/usr/bin/env python3

# СКЕЛЕТ ОСНОВНОЙ ПРОГРАММЫ

import rospy
from numpy import nan, isnan
from sensor_msgs.msg import NavSatFix
import gnss_math as gm

# ====
# УГОЛ
# ====
latitude = nan
longitude = nan


def nav_cb(nsf):
    latitude = nsf.latitude
    longitude = nsf.longitude


rospy.init_node('robot', anonymous=True)
nav = rospy.Subscriber('fix', NavSatFix, nav_cb, queue_size=10)

# ===============
# ПОЛУЧЕНИЕ ТОЧЕК
# ===============
# todo: получаем точки
point_list = [[100, 100][200, 200][300, 300][400, 400]]  # загруженные точки

# ================
# ПРОХОД ПО ТОЧКАМ
# ================
err_dist = 1  # м, допустимая ошибка
err_angl = 15  # градусы, допустимая ошибка
latitude_old = latitude
longitude_old = longitude

for point in point_list:
    while gm.distance((latitude, longitude), (point)) > err_dist:  # Пока не доехали до точки
        dist = gm.distance((latitude, longitude), (point))
        angl = gm.angle((latitude_old, longitude_old),
                        (latitude, longitude),
                        (point))
        # Обновление *_old необходимо сделать в начале итерации, но после всех подсчетов,
        # где необходимы *_old
        latitude_old = latitude
        longitude_old = longitude
        if abs(angl) > err_angl:
            # todo: ПОВЕРНУТЬ
            pass
        # todo: ехать вперед
        # todo: sleep(1)
