# from draw_orbits import draw_orbits
from calculate_distance import calculate_superior_distance, calculate_inferior_distance
from calculate_period import calculate_sidereal_period
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from planet_data import names
from planet_data import synodic_periods
from planet_data import greatest_elongation_angles
from planet_data import quarter_periods

# THINK ABOUT HOW TO RESTRUCTURE MAIN FUNCTION INTO CALLS TO OTHER FUNCTIONS

if __name__ == '__main__':

    earth_sidereal_period = 365.25636  # mean solar days (d)
    astronomical_unit = 1.0


    # data_to_dataframe()
    # Create initial Pandas data frame from planet names
    planets_data = pd.DataFrame(names, columns=['Planet'])

    # Append synodic periods to planets_data data frame
    planets_data['Synodic Period'] = synodic_periods

    # Append "quarter periods" to planets_data data frame
    planets_data['Quarter Period'] = quarter_periods

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
