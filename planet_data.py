earth_sidereal_period = 365.25636  # mean solar days (d)
astronomical_unit = 1.0


def initialize_planet_data ():

    from astropy.time import Time
    import numpy as np
    import pandas as pd

    names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    synodic_periods = [115.88, 583.92, 365.242, 779.94, 398.88, 378.09, 369.66, 367.49]

    greatest_elongation_angles = [0.4014, 0.8029, 0., 3.141, 3.141, 3.141, 3.141, 3.141]

    # Greatest elongation angle (in degrees)
    #   References:
    #       Northcott, R.J., "The Visibility of the Planet Mercury", J. Royal Astro. Soc. Canada 59, 28 (1965).
    #       Colin, L., in Venus, "Basic Facts about Venus" (1983) p. 21.
    greatest_elongations = {
        'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
        'Greatest Elongation': [19.000, 48.000, 0.000, 180.000, 180.000, 180.000, 180.000, 180.000]
    }

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

    # Create initial Pandas data frame from planet names
    planets_data = pd.DataFrame(names, columns=['Planet'])

    # Append synodic periods to planets_data data frame
    planets_data['Synodic Period'] = synodic_periods

    planets_data['Greatest Elongation'] = greatest_elongation_angles

    # generate_quarter_periods()
    #       Takes opposition and eastern quadrature times
    #       Returns list of quarter periods
    quarter_periods = [0., 0., 0.]  # initialize with zeros for Mercury through Earth
    for planet in planet_times:
        opposition_times = Time(planet_times[planet]['opposition'])
        quadrature_times = Time(planet_times[planet]['eastern_quadrature'])
        quarter_period = np.mean(quadrature_times.jd - opposition_times.jd)
        quarter_periods.append(quarter_period)

    # Append "quarter periods" to planets_data data frame
    planets_data['Quarter Period'] = quarter_periods

    return planets_data


