def calculate_sidereal_period(synodic_period, is_inferior, reference_synodic_period=365.242):
    try:
        if is_inferior:
            sidereal_period = 1./((1./synodic_period) + (1./reference_synodic_period))
        else:
            sidereal_period = 1./((1./reference_synodic_period) - (1./synodic_period))
    except ZeroDivisionError:
        print("Error: zero is an invalid period value")
        sidereal_period = 0.
    finally:
        return sidereal_period


def calculate_sidereal_periods_and_solar_distances(planets_data):
    from calculate_distance import calculate_inferior_distance, calculate_superior_distance
    from planet_data import astronomical_unit, earth_sidereal_period
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
    planets_data['Solar Distance'] = solar_distances
    return planets_data

