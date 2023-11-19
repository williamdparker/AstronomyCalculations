import matplotlib.pyplot as plt
from astropy.time import Time
import matplotlib
import numpy as np


def draw_phase(illumination, radius, center=[0, 0], phase='waxing'):
    dihedral_angle = np.arccos(-2 * illumination + 1)
    if phase == 'waxing':
        central_angles = np.linspace(-np.pi / 2, np.pi / 2, num=1_000)
    else:
        central_angles = np.linspace(np.pi / 2, 3*np.pi / 2, num=1_000)
    x_values = radius * np.cos(dihedral_angle) * np.cos(central_angles) + center[0]
    y_values = radius * np.sin(central_angles) + center[1]
    # plt.plot(x_values, y_values, color='black')
    plt.fill_betweenx(y_values, x_values, radius*np.cos(central_angles) + center[0],
                      color='cornsilk', linewidth=0)
    return


def draw_moon(radius, center, label=''):
    central_angles = np.linspace(0, 2 * np.pi, num=1_000)
    plt.plot(radius * np.cos(central_angles) + center[0], radius * np.sin(central_angles) + center[1],
             color='black', linewidth=0.5)
    plt.fill_between(radius*np.cos(central_angles[:500])+center[0],
                     radius*np.sin(central_angles[:500])+center[1],
                     radius*np.sin(central_angles[500:])+center[1],
                     color='black', alpha=1.0)

    if len(label) > 0:
        if center[0] > 0.:
            horizontal_alignment = 'left'
            label_x = center[0] + radius
        elif center[0] < 0.:
            horizontal_alignment = 'right'
            label_x = center[0] - radius
        else:
            horizontal_alignment = 'center'
            label_x = center[0] + radius
        if center[1] > 0.:
            vertical_alignment = 'bottom'
            label_y = center[1] + radius
        elif center[1] < 0.:
            vertical_alignment = 'top'
            label_y = center[1] - radius
        else:
            vertical_alignment = 'center'
            label_y = center[1]
        plt.text(label_x, label_y, label, color='black', ha=horizontal_alignment, va=vertical_alignment)
    return


def draw_lunar_cycle(file_name=''):
    moon_radius = 1
    drawing_radius = 17 * moon_radius
    number_of_days = 29

    sidereal_period = 27.32
    tropical_year = 365.26
    day_to_elongation_angle = 2 * np.pi * (tropical_year - sidereal_period) / (tropical_year * sidereal_period)
    # Create a plot and add the circle and terminator arc
    fig, ax = plt.subplots(figsize=(10, 10))

    # days = np.arange(int(number_of_days/2))
    days = np.arange(number_of_days)
    for day in days:
        drawing_angle = day * 2 * np.pi / number_of_days + np.pi/20
        moon_center = drawing_radius * np.array([np.cos(drawing_angle), np.sin(drawing_angle)])
        draw_moon(moon_radius, center=moon_center, label=str(day+1))
        illumination = 0.5 * (1 - np.cos(day * day_to_elongation_angle))
        if day < number_of_days/2:
            draw_phase(illumination, moon_radius, center=moon_center, phase='waxing')
        else:
            draw_phase(illumination, moon_radius, center=moon_center, phase='waning')


    # Set equal scaling and remove axes
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    # Show the plot
    ax.set_xlim([-1.2 * drawing_radius, 1.2 * drawing_radius])
    ax.set_ylim([-1.2 * drawing_radius, 1.2 * drawing_radius])
    if len(file_name) == 0:
        plt.show()
    else:
        plt.savefig(file_name)
    return


if __name__ == '__main__':
    matplotlib.use('macosx')
    plt.style.use('calendar_sign.mplstyle')
    # draw_lunar_cycle()
    draw_lunar_cycle(file_name='LunarPhasesAndDays.svg')
