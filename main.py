from calculate_period import calculate_sidereal_periods_and_solar_distances
from planet_data import initialize_planet_data
from plot_data import plot_period_vs_distance


def main():
    planets_data = initialize_planet_data()

    planets_data = calculate_sidereal_periods_and_solar_distances(planets_data)

    plot_period_vs_distance(planets_data)


if __name__ == '__main__':
    main()
