# from draw_orbits import draw_orbits
from calculate_distance import calculate_superior_distance, calculate_inferior_distance
from calculate_period import calculate_sidereal_period
from astropy.time import Time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# THINK ABOUT HOW TO RESTRUCTURE MAIN FUNCTION INTO CALLS TO OTHER FUNCTIONS


if __name__ == '__main__':

    earth_sidereal_period = 365.25636  # mean solar days (d)
    astronomical_unit = 1.0

    ###### MOVE TO SEPARATE FILE "planet_data" and import ######
    # Values from JPL HORIZONS
    # Include five data points per planet (Mars, Jupiter, Saturn, Uranus, Neptune)
    planet_times = {
        'mars': {
            'opposition': ['2018-07-27T00:00',
                           '2020-10-14T00:00',
                           '2022-12-08T00:00',
                           '2025-01-16T00:00',
                           '2027-02-20T00:00'],
            'eastern_quadrature': ['2018-12-02T00:00',
                                   '2021-02-01T00:00',
                                   '2023-03-17T00:00',
                                   '2025-04-21T00:00',
                                   '2027-05-26T00:00']
        },
        'jupiter': {
            'opposition': ['2018-05-09T00:00',
                           '2019-06-11T00:00',
                           '2020-07-14T00:00',
                           '2021-08-20T00:00',
                           '2022-09-27T00:00'],
            'eastern_quadrature': ['2018-08-07T00:00',
                                   '2019-09-09T00:00',
                                   '2020-10-12T00:00',
                                   '2021-11-16T00:00',
                                   '2022-12-22T00:00']
        },
        'saturn': {
            'opposition': ['2018-06-28T00:00',
                           '2019-07-10T00:00',
                           '2020-07-21T00:00',
                           '2021-08-02T00:00',
                           '2022-08-15T00:00'],
            'eastern_quadrature': ['2018-09-26T00:00',
                                   '2019-10-06T00:00',
                                   '2020-10-19T00:00',
                                   '2021-10-30T00:00',
                                   '2022-11-11T00:00']
        },
        'uranus': {
            'opposition': ['2018-10-24T00:00',
                           '2019-10-28T00:00',
                           '2020-11-01T00:00',
                           '2021-11-05T00:00',
                           '2022-11-09T00:00'],
            'eastern_quadrature': ['2019-01-19T00:00',
                                   '2020-01-23T00:00',
                                   '2021-01-27T00:00',
                                   '2022-01-31T00:00',
                                   '2023-02-04T00:00']
        },
        'neptune': {
            'opposition': ['2018-09-08T00:00',
                           '2019-09-10T00:00',
                           '2020-09-12T00:00',
                           '2021-09-14T00:00',
                           '2022-09-17T00:00'],
            'eastern_quadrature': ['2018-12-06T00:00',
                                   '2019-12-08T00:00',
                                   '2020-12-10T00:00',
                                   '2021-12-12T00:00',
                                   '2022-12-15T00:00']
        },
    }

    # generate_quarter_periods()
    #       Takes opposition and eastern quadrature times
    #       Returns list of quarter periods
    quarter_periods = [0., 0., 0.]  # initialize with zeros for Mercury through Earth
    for planet in planet_times:
        opposition_times = Time(planet_times[planet]['opposition'])
        quadrature_times = Time(planet_times[planet]['eastern_quadrature'])
        quarter_period = np.mean(quadrature_times.jd - opposition_times.jd)
        quarter_periods.append(quarter_period)

    ###### MOVE TO SEPARATE FILE "planet_data" and import ######
    synodic_periods = {'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                       'Synodic Period': [115.88, 583.92, 365.242, 779.94, 398.88, 378.09, 369.66, 367.49]
                       }

    # data_to_dataframe()
    # Turn synodic periods into Pandas DataFrame
    planets_data = pd.DataFrame(synodic_periods, columns=['Planet', 'Synodic Period'])

    # Append "quarter periods" to planets_data data frame
    planets_data['Quarter Period'] = quarter_periods

    ###### MOVE TO SEPARATE FILE "planet_data" and import ######
    greatest_elongation_angles = [0.4014, 0.8029, 0., 3.141, 3.141, 3.141, 3.141, 3.141]

    planets_data['Greatest Elongation'] = greatest_elongation_angles

    # calculate_sidereal_periods()
    # Calculate the sidereal period from synodic periods
    sidereal_periods = []
    solar_distances = []
    for index in planets_data.index:
        period = planets_data['Synodic Period'][index]
        planet = planets_data['Planet'][index]
        if planet == 'Mercury' or planet == 'Venus':
            sidereal_periods.append(calculate_sidereal_period(period, is_inferior=True))
            solar_distances.append(calculate_inferior_distance(planets_data['Greatest Elongation'][index]))
        elif planet == 'Earth':
            sidereal_periods.append(earth_sidereal_period)
            solar_distances.append(astronomical_unit)
        else:
            sidereal_periods.append(calculate_sidereal_period(period, is_inferior=False))
            solar_distances.append(calculate_superior_distance(planets_data['Quarter Period'][index],
                                                               sidereal_periods[index]))

    planets_data['Sidereal Period'] = sidereal_periods

    # solar_distances = [0.387, 0.723, 1.00, 1.52, 5.20, 9.58, 19.20, 30.05]
    print(solar_distances)
    planets_data['Solar Distance'] = solar_distances

    # plot_period_vs_distance()
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
