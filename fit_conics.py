import numpy as np


def conic_function(x, y, parameters):
    # 𝑎𝑥^2+2ℎ𝑥𝑦+𝑏𝑦^22+2𝑔𝑥+2𝑓𝑦+1=0
    # Wikipedia notation:
    #   Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0
    # parameters = [a, b, f, g, h]
    #               0, 1, 2, 3, 4
    conic = parameters[0]*x**2 + 2*parameters[4]*x*y + parameters[1]*y**2 + 2*parameters[3]*x + 2*parameters[2]*y + 1
    return conic



# def least_squares()
