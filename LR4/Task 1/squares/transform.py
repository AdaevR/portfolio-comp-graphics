import numpy as np
import math as m

def translate(x: float, y: float):
    return np.array([
        [ 1, 0, 0],
        [ 0, 1, 0],
        [ x, y, 1]
    ])

def scale(x: float, y: float):
    return np.array([
        [ x, 0, 0],
        [ 0, y, 0],
        [ 0, 0, 1]
    ])

def rotate(angle: float):
    cs = m.cos(angle)
    sn = m.sin(angle)
    return np.array([
        [ cs, sn, 0],
        [-sn, cs, 0],
        [ 0, 0, 1]
    ])
