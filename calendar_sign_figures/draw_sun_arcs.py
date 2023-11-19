import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Circle, FancyArrow
from matplotlib.colors import ListedColormap
import numpy as np
from astropy.coordinates import EarthLocation, AltAz, get_sun
from astropy.time import Time
import astropy.units as u
from astroplan import Observer


def calculate_extreme_declination_times(year):
    # Instantiate astropy Time objects at start and end of year
    start_time = Time(f'{year}-01-01 00:00:00', format='iso')
    end_time = Time(f'{year + 1}-01-01 00:00:00', format='iso')

    # Instantiate a Time object that incorporates the entire year of dates as an NumPy array
    times = Time(np.linspace(start_time.jd, end_time.jd, 365), format='jd')

    # Find dates of maximum and minimum declination
    max_declination_time = times[np.argmax(get_sun(times).dec)]
    min_declination_time = times[np.argmin(get_sun(times).dec)]

    # Calculate solar positions on the dates of extreme declinations
    extreme_times = [max_declination_time, min_declination_time]
    return extreme_times


def calculate_sun_arc_of_date(julian_date, observer_location, location_name=""):
    # Instantiate astroplan Observer object from astropy EarthLocation
    observer = Observer(location=observer_location, name=location_name)

    # Convert Julian date to astropy Time object
    time = Time(julian_date, format='jd')

    # Get sunrise and sunset times for the nearest sunrise to the date and the subsequent sunset
    sunrise_time = observer.sun_rise_time(time, which='nearest')
    sunset_time = observer.sun_set_time(sunrise_time, which='next')

    # Set up array of times between sunrise and sunset to calculate horizontal coordinates of Sun
    times = np.linspace(sunrise_time, sunset_time, num=100)

    # Initialize horizontal coordinate lists
    azimuths = []
    altitudes = []

    # Loop over times, calculate the Sun horizontal coordinates and append to the lists
    for time in times:
        azimuth = float(observer.sun_altaz(time).to_string(decimal=True).split()[0])
        azimuths.append(azimuth)
        altitude = float(observer.sun_altaz(time).to_string(decimal=True).split()[1])
        altitudes.append(altitude)
    return altitudes, azimuths


def draw_sun_arcs(arcs, file_name=''):
    # Define ranges of horizontal coordinates
    minimum_azimuth, maximum_azimuth = 45, 315
    azimuth_range = maximum_azimuth - minimum_azimuth
    minimum_altitude, maximum_altitude = -10, 240
    altitude_range = maximum_altitude - minimum_altitude

    # Create plot
    figure, axes = plt.subplots(figsize=(6, 6))
    # Use custom matplotlib style
    plt.style.use('calendar_sign.mplstyle')
    # Create custom color map for the summer and winter Sun
    custom_colors = ['darkorange', 'gold']
    # custom_colormap = ListedColormap(['orange', 'yellow'])

    # Add white space
    whitespace_factor = 0.03
    axes.set(
        xlim=[minimum_azimuth - whitespace_factor * azimuth_range,
              maximum_azimuth + whitespace_factor * azimuth_range],
        ylim=[minimum_altitude - whitespace_factor * altitude_range,
              maximum_altitude + whitespace_factor * altitude_range]
    )

    # Label cardinal directions
    directions = {'East': 90, 'South': 180, 'West': 270}
    for direction, azimuth in directions.items():
        plt.text(azimuth, -0.01 * azimuth_range, direction, ha='center', va='top')

    # Draw horizon
    plt.plot([minimum_azimuth, maximum_azimuth], [0, 0], color='black')

    # Draw hour segments
    minimum_hour = np.ceil(minimum_azimuth * (24 / 360))
    maximum_hour = np.ceil(maximum_azimuth * (24 / 360))
    for hour in np.arange(minimum_hour, maximum_hour + 1):
        hour_azimuth = hour * (360 / 24)
        plt.plot([hour_azimuth, hour_azimuth], [0, maximum_altitude],
                 color='black', alpha=0.1)

        # Label hour segments
        #    Standard time
        if hour == 12:
            hour_label = 'noon'
        elif hour < 12:
            hour_label = str(int(hour)) + ' am'
        else:
            hour_label = str(int(hour - 12)) + ' pm'
        extreme_hours = [8, 12, 12+4]
        if hour not in extreme_hours:
            plt.text(hour_azimuth, maximum_altitude - 0.2 * altitude_range, hour_label,
                 rotation=90, ha='right', va='top', alpha=0.5)
        else:
            plt.text(hour_azimuth, maximum_altitude - 0.2 * altitude_range, hour_label,
                     rotation=90, ha='right', va='top', alpha=0.5, color=custom_colors[1])
        #   Daylight time
        daylight_time_hour = hour + 1
        if daylight_time_hour == 12:
            daylight_time_hour_label = 'noon'
        elif daylight_time_hour < 12:
            daylight_time_hour_label = str(int(daylight_time_hour)) + ' am'
        else:
            daylight_time_hour_label = str(int(daylight_time_hour - 12)) + ' pm'
        extreme_hours = [5, 12+1, 12+9]
        if daylight_time_hour not in extreme_hours:
            plt.text(hour_azimuth, maximum_altitude, daylight_time_hour_label,
                     rotation=90, ha='right', va='top', alpha=0.5)
        else:
            plt.text(hour_azimuth, maximum_altitude, daylight_time_hour_label,
                     rotation=90, ha='right', va='top', alpha=0.5, color=custom_colors[0])

    plt.text((minimum_hour - 1) * (360 / 24), maximum_altitude, 'Daylight Time',
             ha='left', va='bottom', alpha=0.7)
    plt.text((minimum_hour - 1) * (360 / 24), maximum_altitude - 0.35 * altitude_range, 'Standard Time',
             ha='left', va='top', alpha=0.7)

    arc_labels = ['Summer Solstice', 'Winter Solstice']
    for arc_index, arc in enumerate(arcs):
        # Draw arcs
        arc_curve, = plt.plot(arc[0], arc[1], color=custom_colors[arc_index])

        # Plot sun icons at culmination
        culmination_index = np.argmax(arc[1])
        culmination_sun_icon = Circle((180, arc[1][culmination_index]),
                          radius=0.02 * azimuth_range, color=arc_curve.get_color())
        axes.add_patch(culmination_sun_icon)

        # Plot sun icons at sunrise
        sunrise_index = np.argmin(arc[0])
        sunrise_sun_icon = Circle((arc[0][sunrise_index], 0),
                    radius=0.02 * azimuth_range, color=arc_curve.get_color())
        axes.add_patch(sunrise_sun_icon)

        # Plot sun icons at sunset
        sunset_index = np.argmax(arc[0])
        sunset_sun_icon = Circle((arc[0][sunset_index], 0),
                    radius=0.02 * azimuth_range, color=arc_curve.get_color())
        axes.add_patch(sunset_sun_icon)

        # Plot ascending arrow
        ascending_midpoint_index = int(0.5*(sunrise_index + culmination_index))
        arrow_delta = np.array([arc[0][ascending_midpoint_index + 1] - arc[0][ascending_midpoint_index - 1],
                       arc[1][ascending_midpoint_index + 1] - arc[1][ascending_midpoint_index - 1]])
        arrow_delta = arrow_delta / np.linalg.norm(arrow_delta)
        ascending_arrow = FancyArrow(arc[0][ascending_midpoint_index], arc[1][ascending_midpoint_index],
                                     arrow_delta[0], arrow_delta[1], width=0.005*azimuth_range, color=arc_curve.get_color())
        axes.add_patch(ascending_arrow)

        # Plot descending arrow
        descending_midpoint_index = int(0.5*(sunset_index + culmination_index))
        arrow_delta = np.array([arc[0][descending_midpoint_index + 1] - arc[0][descending_midpoint_index - 1],
                       arc[1][descending_midpoint_index + 1] - arc[1][descending_midpoint_index - 1]])
        arrow_delta = arrow_delta / np.linalg.norm(arrow_delta)
        descending_arrow = FancyArrow(arc[0][descending_midpoint_index], arc[1][descending_midpoint_index],
                                     arrow_delta[0], arrow_delta[1], width=0.005*azimuth_range, color=arc_curve.get_color())
        axes.add_patch(descending_arrow)

        # Label arc
        plt.text(arc[0][culmination_index], arc[1][culmination_index]+0.02*altitude_range, arc_labels[arc_index],
                 color=arc_curve.get_color(), ha='center', va='bottom')


    # Label sunrises and sunsets
    plt.text(90+2.5, 0.025*altitude_range, 'Sunrise',
             ha='center', va='center', alpha=0.5)
    plt.text(270-2.5, 0.025 * altitude_range, 'Sunset',
             ha='center', va='center', alpha=0.5)

    # Turn off the axes
    axes.axis('off')

    # Make ratio equal
    axes.set_aspect('equal')
    # Show the plot or write out the file
    if len(file_name) == 0:
        plt.show()
    else:
        plt.savefig(file_name)
    return


if __name__ == '__main__':
    # matplotlib.use('macosx')

    observatory_location = EarthLocation(lat=42.650033 * u.deg, lon=-87.878774 * u.deg, height=200 * u.m)
    year = 2023

    sun_arcs = []
    solstice_times = calculate_extreme_declination_times(year)
    for solstice_time in solstice_times:
        sun_arc_altitudes, sun_arc_azimuths = calculate_sun_arc_of_date(solstice_time, observatory_location)
        sun_arcs.append([sun_arc_azimuths, sun_arc_altitudes])

    draw_sun_arcs(sun_arcs)
    # draw_sun_arcs(sun_arcs, file_name='SunArcsAndTimes.svg')
