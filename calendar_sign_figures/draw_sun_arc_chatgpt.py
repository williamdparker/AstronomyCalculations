import numpy as np
import matplotlib.pyplot as plt

def calculate_solar_coordinates(latitude, longitude, day_of_year, num_points=96):
    times = np.linspace(0, 24, num_points)  # Hours from midnight to midnight
    altitudes, azimuths = [], []

    for hour in times:
        # Calculate solar coordinates for each hour
        altitude, azimuth = calculate_solar_coordinates_at_hour(latitude, longitude, day_of_year, hour)
        altitudes.append(altitude)
        azimuths.append(azimuth)

    return times, altitudes, azimuths

def calculate_solar_coordinates_at_hour(latitude, longitude, day_of_year, hour):
    # Step 1: Calculate the number of days from the vernal equinox
    n = day_of_year

    # Step 2: Calculate the mean longitude of the Sun
    L0 = 280.46646 + 0.9856474 * n

    # Step 3: Calculate the Sun's apparent longitude
    g = (357.528 + 0.9856003 * n) % 360

    # Step 4: Calculate the Sun's declination
    declination = np.degrees(np.arcsin(np.sin(np.radians(23.43929)) * np.sin(np.radians(g))))

    # Step 5: Calculate the observer's hour angle
    H = 15 * (hour - 12 - (longitude + L0) / 15)

    # Step 6: Calculate the observer's latitude and the Sun's hour angle
    phi = np.radians(latitude)
    delta = np.radians(declination)
    H = np.radians(H)

    # Step 7: Calculate the altitude and azimuth of the Sun
    altitude = np.degrees(np.arcsin(np.sin(phi) * np.sin(delta) + np.cos(phi) * np.cos(delta) * np.cos(H)))
    azimuth = np.degrees(np.arctan2(-np.sin(H), np.tan(delta) * np.cos(phi) - np.sin(phi) * np.cos(H)))

    # Adjust azimuth to be between 0 and 360 degrees
    azimuth = (azimuth + 360) % 360

    return altitude, azimuth

# Example usage:
latitude = 43.0  # Observer's latitude in degrees
longitude = -87.0  # Observer's longitude in degrees
day_of_year = 172  # Day of the year (e.g., June 21)



# Plot the solar path
plt.figure(figsize=(10, 6))
for day in range(295, 305):
    times, altitudes, azimuths = calculate_solar_coordinates(latitude, longitude, day)
    plt.plot(azimuths, altitudes, label=f'Day {day}')
plt.xlabel('Azimuth (degrees')
plt.ylabel('Altitude (degrees)')
plt.title('Solar Path Across the Sky')
plt.legend()
plt.grid(True)
plt.ylim([0, 90])
plt.show()
