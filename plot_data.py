def plot_period_vs_distance(planets_data):
    import matplotlib.pyplot as plt
    import numpy as np
    from planet_data import earth_sidereal_period

    plt.scatter(np.log(planets_data['Sidereal Period'] / earth_sidereal_period), np.log(planets_data['Solar Distance']))
    plt.xlabel('ln(Sidereal period (y))')
    plt.ylabel('ln(Solar distance (au))')

    # plt.xscale('log')
    # plt.yscale('log')
    x_max = np.max(np.log(planets_data['Sidereal Period'] / earth_sidereal_period))
    x_min = np.min(np.log(planets_data['Sidereal Period'] / earth_sidereal_period))
    # x_values = np.logspace(-2.0, 1.5, num=int(1e4))
    x_values = np.linspace(x_min, x_max)

    power_ratio = 2. / 3.
    intercept_coefficient = 0.
    y_values = power_ratio * x_values + intercept_coefficient

    plt.plot(x_values, y_values)
    plt.show()

    return
