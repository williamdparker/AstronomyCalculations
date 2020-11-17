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




