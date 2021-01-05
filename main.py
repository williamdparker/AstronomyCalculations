# from draw_orbits import draw_orbits
from calculate_distance import calculate_superior_distance
from calculate_period import calculate_sidereal_period
from astropy.time import Time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    earth_sidereal_period = 365.25636  # mean solar days (d)

    # Values for Jupiter from JPL HORIZONS
    #   2020-Jul-14 179.5137 elongation
    #   2021-Aug-20 178.8157 elongation
    #   2022-Sep-27 178.3660 elongation
    # opposition_times = ['2020-07-14T00:00', '2021-08-20T00:00', '2022-09-27T00:00']
    # eastern_quadrature_times = ['2020-10-12T00:00', '2021-11-16T00:00', '2022-12-22T00:00']

    # Include five data points per planet (Mars, Jupiter, Saturn, Uranus, Neptune)
    planet_times = {
        'jupiter': {
            'opposition': ['2018-05-09T00:00', '2020-07-14T00:00', '2021-08-20T00:00'],
            'eastern_quadrature': ['2018-08-07T00:00', '2020-10-12T0:00', '2021-11-16T00:00']
        },
        'saturn': {
            'opposition': ['2018-05-09T00:00', '2020-07-14T00:00', '2021-08-20T00:00'],
            'eastern_quadrature': ['2018-08-07T00:00', '2020-10-12T0:00', '2021-11-16T00:00']
        }
    }

    quarter_periods = [0., 0., 0.]  # initialize with zeros for Mercury through Earth
    for planet in planet_times:
        opposition_times = Time(planet_times[planet]['opposition'])
        quadrature_times = Time(planet_times[planet]['eastern_quadrature'])
        quarter_period = np.mean(quadrature_times.jd - opposition_times.jd)
        quarter_periods.append(quarter_period)

    synodic_periods = {'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                       'Synodic Period': [115.88, 583.92, 365.242, 779.94, 398.88, 378.09, 369.66, 367.49]
                       }

    # Turn synodic periods into Pandas DataFrame

    planets_data = pd.DataFrame(synodic_periods, columns=['Planet', 'Synodic Period'])

    # Append "quarter periods" to planets_data data frame
    # planets_data['Quarter Period'] = np.array(quarter_periods)

    # Calculate the sidereal period from synodic periods
    sidereal_periods = []
    for index in planets_data.index:
        period = planets_data['Synodic Period'][index]
        planet = planets_data['Planet'][index]
        if planet == 'Mercury' or planet == 'Venus':
            sidereal_periods.append(calculate_sidereal_period(period, is_inferior=True))
        elif planet == 'Earth':
            sidereal_periods.append(earth_sidereal_period)
        else:
            sidereal_periods.append(calculate_sidereal_period(period, is_inferior=False))

    planets_data['Sidereal Period'] = np.array(sidereal_periods)
    solar_distances = [0.387, 0.723, 1.00, 1.52, 5.20, 9.58, 19.20, 30.05]
    planets_data['Solar Distance'] = np.array(solar_distances)
    plt.scatter(np.log(planets_data['Sidereal Period'] / earth_sidereal_period), np.log(planets_data['Solar Distance']))
    plt.xlabel('ln(Sidereal period (y))')
    plt.ylabel('ln(Solar distance (au))')
    # plt.xscale('log')
    # plt.yscale('log')
    x_max = np.max(np.log(planets_data['Sidereal Period'] / earth_sidereal_period))
    x_min = np.min(np.log(planets_data['Sidereal Period'] / earth_sidereal_period))
    # x_values = np.logspace(-2.0, 1.5, num=int(1e4))
    x_values = np.linspace(x_min, x_max)
    power_ratio = 2./3.
    intercept_coefficient = 0.
    y_values = power_ratio * x_values + intercept_coefficient
    plt.plot(x_values, y_values)
    plt.show()

    # jupiter_sidereal_period = calculate_sidereal_period(earth_synodic_period, jupiter_synodic_period)

    # Calculate relative distance from Sun using quarter period
    # jupiter_relative_distance = calculate_superior_distance(jupiter_quarter_period, jupiter_sidereal_period)
    # print(jupiter_relative_distance)
