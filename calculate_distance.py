import numpy as np


def calculate_superior_distance(quadrature_time, planet_sidereal_period,
                                earth_sidereal_period=365.256, earth_sun_distance=1.):
    # define alpha
    alpha = (quadrature_time * (2 * np.pi / earth_sidereal_period))

    # define beta
    beta = (quadrature_time * (2 * np.pi) / planet_sidereal_period)

    return earth_sun_distance / np.cos(alpha - beta)


def calculate_inferior_distance(greatest_elongation, earth_sun_distance=1.):
    return earth_sun_distance * np.sin(greatest_elongation)
