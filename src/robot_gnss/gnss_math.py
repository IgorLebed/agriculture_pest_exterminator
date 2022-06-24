#!/usr/bin/env python3

from math import acos, asin, sin, sqrt, degrees, radians
from numpy import nan

# https://en.wikipedia.org/wiki/Great-circle_distance
# https://math.stackexchange.com/questions/1027476/calculating-clockwise-anti-clockwise-angles-from-a-point


def distance(p_t0, p_t1):
    """ Возвращает расстояние между точками или nan

    p_t0, p_t1, p_want = (latitude, longitude)"""
    # Vincenty formula
    delta_lambda = p_t0[1] - p_t1[1]
    delta_phi = p_t0[0] - p_t1[0]
    delta_sigma = 2 * asin(sqrt(sin(delta_phi/2)**2 + (1 - sin(delta_phi/2)**2 - sin((p_t0[0] + p_t1[0])/2)**2)*sin(delta_lambda/2)**2))
    # Distance
    r = 6371.009  # km
    return r * delta_sigma


def angle(p_t0, p_t1, p_want):
    """ Возвращает угол между нынешним направлением и желаемым или nan

    p_t0, p_t1, p_want = (latitude, longitude)"""
    if p_t0 == p_t1 or p_t0 == p_want or p_t1 == p_want:
        return 0

    p_t0_calc = [radians(p_t0[0]), radians(p_t0[1])]
    p_t1_calc = [radians(p_t1[0]), radians(p_t1[1])]
    p_want_calc = [radians(p_want[0]), radians(p_want[1])]

    d_01 = distance(p_t0_calc, p_t1_calc)
    d_0want = distance(p_t0_calc, p_want_calc)
    d_1want = distance(p_t1_calc, p_want_calc)

    # Direction
    p_t1_calc = [radians(p_t1[0])-radians(p_t0[0]), radians(p_t1[1])-radians(p_t0[1])]
    p_want_calc = [radians(p_want[0])-radians(p_t0[0]), radians(p_want[1])-radians(p_t0[1])]
    p_t0_calc = [0, 0]
    direction = p_t1_calc[0]*p_want_calc[1] - p_t1_calc[1]*p_want_calc[0]
    direction = direction / abs(direction)

    angle = acos((d_01**2 + d_0want**2 - d_1want**2)/(2*d_01*d_0want)) * direction
    return degrees(angle)


if __name__ == '__main__':
    # Вверх и вправо
    print(angle((59.947365, 30.303307),
                (59.947354, 30.300042),
                (59.947016, 30.303308)))
    # Наоборот
    print(angle((59.935954, 30.285555),
                (59.936062, 30.285555),
                (59.935954, 30.285247)))
    # По диагонали (северо-восток, юго-запад)
    print(angle((59.947365, 30.303307),
                (59.947121, 30.303793),
                (59.947213, 30.303005)))

    # ~45
    print(angle((59.946213, 30.271605),
                (59.942405, 30.275963),
                (59.940679, 30.267856)))

    # Совпадения
    print(angle((59.916990, 30.337972),
                (59.916990, 30.337972),
                (59.916990, 30.337972)))

    # nan
    print(angle((59.947365, 30.303307),
                (nan, nan),
                (59.947213, 30.303005)))
