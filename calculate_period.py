def calculate_sidereal_period(inferior_period, superior_period):
    try:
        sidereal_period = 1./((1./inferior_period) - (1./superior_period))
    except ZeroDivisionError:
        print("Error: zero is an invalid period value")
        sidereal_period = 0.
    finally:
        return sidereal_period




