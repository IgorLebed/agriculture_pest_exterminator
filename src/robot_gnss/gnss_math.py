#!/usr/bin/env python3

from math import acos, asin, sin, sqrt, degrees, radians
from numpy import nan


def distance(p_t0, p_t1):
    """ Returns the distance between points or nan

    p_t0, p_t1 = (latitude, longitude)"""
    # Haversine formula
    delta_lambda = p_t0[1] - p_t1[1]
    delta_phi = p_t0[0] - p_t1[0]
    delta_sigma = 2 * asin(sqrt(sin(delta_phi/2)**2 + (1 - sin(delta_phi/2)**2 - sin((p_t0[0] + p_t1[0])/2)**2)*sin(delta_lambda/2)**2))
    # Great-circle distance
    r = 6371.009  # km
    return r * delta_sigma


def angle(p_t0, p_t1, p_desired):
    """ Returns the angle between the current direction and the desired one or nan

    p_t0, p_t1, p_desired = (latitude, longitude)"""
    if p_t0 == p_t1 or p_t0 == p_desired or p_t1 == p_desired:
        return 0

    p_t0_calc = [radians(p_t0[0]), radians(p_t0[1])]
    p_t1_calc = [radians(p_t1[0]), radians(p_t1[1])]
    p_desired_calc = [radians(p_desired[0]), radians(p_desired[1])]

    d_01 = distance(p_t0_calc, p_t1_calc)
    d_0desired = distance(p_t0_calc, p_desired_calc)
    d_1desired = distance(p_t1_calc, p_desired_calc)

    # Direction
    # https://math.stackexchange.com/questions/1027476/calculating-clockwise-anti-clockwise-angles-from-a-point
    p_t1_calc = [radians(p_t1[0])-radians(p_t0[0]), radians(p_t1[1])-radians(p_t0[1])]
    p_desired_calc = [radians(p_desired[0])-radians(p_t0[0]), radians(p_desired[1])-radians(p_t0[1])]
    p_t0_calc = [0, 0]
    direction = p_t1_calc[0]*p_desired_calc[1] - p_t1_calc[1]*p_desired_calc[0]
    direction = direction / abs(direction)

    angle = acos((d_01**2 + d_0desired**2 - d_1desired**2)/(2*d_01*d_0desired)) * direction
    return degrees(angle)


if __name__ == '__main__':
    # TESTS
    # North and east
    print(angle((59.947365, 30.303307),
                (59.947354, 30.300042),
                (59.947016, 30.303308)))
    # Conversely
    print(angle((59.935954, 30.285555),
                (59.936062, 30.285555),
                (59.935954, 30.285247)))
    # Diagonally (northeast, southwest)
    print(angle((59.947365, 30.303307),
                (59.947121, 30.303793),
                (59.947213, 30.303005)))

    # ~45
    print(angle((59.946213, 30.271605),
                (59.942405, 30.275963),
                (59.940679, 30.267856)))

    # Coincidences
    print(angle((59.916990, 30.337972),
                (59.916990, 30.337972),
                (59.916990, 30.337972)))

    # nan
    print(angle((59.947365, 30.303307),
                (nan, nan),
                (59.947213, 30.303005)))
