# from draw_orbits import draw_orbits
from calculate_distance import calculate_superior_distance
from calculate_period import calculate_sidereal_period
from astropy.time import Time
import numpy as np
import pandas as pd

if __name__ == '__main__':

    # Values for Jupiter from JPL HORIZONS
    #   2020-Jul-14 179.5137 elongation
    #   2021-Aug-20 178.8157 elongation
    #   2022-Sep-27 178.3660 elongation
    # opposition_times = ['2020-07-14T00:00', '2021-08-20T00:00', '2022-09-27T00:00']
    # eastern_quadrature_times = ['2020-10-12T00:00', '2021-11-16T00:00', '2022-12-22T00:00']

    # Convert lists into astropy Time arrays
    # jupiter_opposition_times = Time(opposition_times)
    # jupiter_quadrature_times = Time(eastern_quadrature_times)

    # Calculate periods from Time arrays
    # jupiter_synodic_period = np.mean(np.diff(jupiter_opposition_times.jd))
    # jupiter_quarter_period = np.mean(jupiter_quadrature_times.jd-jupiter_opposition_times.jd)

    synodic_periods = {'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                       'Period': [115.88, 583.92, 365.242, 779.94, 398.88, 378.09, 369.66, 367.49],
                       'Opposition Time': [0, 0, 0, 797.5, 398.5, 377, 369.5, 367.5],
                       'Quadrature Time': [0, 0, 0, 782, 398.5, 376.5, 369, 367.5]
                       }

    planets_data = pd.DataFrame(synodic_periods, columns=['Planet', 'Period', 'Opposition Time', 'Quadrature Time'])

    # Calculate the sidereal period from synodic periods
    sidereal_periods = []
    for index in planets_data.index:
        period = planets_data['Period'][index]
        planet = planets_data['Planet'][index]
        if planet == 'Mercury' or planet == 'Venus':
            sidereal_periods.append(calculate_sidereal_period(period, is_inferior=True))
        elif planet == 'Earth':
            sidereal_periods.append(365.256)
        else:
            sidereal_periods.append(calculate_sidereal_period(period, is_inferior=False))

    print(planets_data)

    # jupiter_sidereal_period = calculate_sidereal_period(earth_synodic_period, jupiter_synodic_period)

    # Calculate relative distance from Sun using quarter period
    # jupiter_relative_distance = calculate_superior_distance(jupiter_quarter_period, jupiter_sidereal_period)
    # print(jupiter_relative_distance)
