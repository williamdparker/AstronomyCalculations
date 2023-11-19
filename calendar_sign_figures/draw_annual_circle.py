from calendar import month_name
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def draw_annual_circle(file_name=''):
    figure, axes = plt.subplots(figsize=(8, 8))
    radius = 1
    axes.set_xlim(-1.25 * radius, 1.25 * radius)
    axes.set_ylim(-1.25 * radius, 1.25 * radius)
    calendar_circle = Circle((0, 0), 0.95*radius, edgecolor='black', facecolor='None')
    axes.add_patch(calendar_circle)
    draw_months_in_circle(radius, axes)
    draw_solstice_equinox_marks(radius)
    axes.set_aspect('equal', adjustable='box')
    plt.axis('off')
    if len(file_name) == 0:
        plt.show()
    else:
        plt.savefig(file_name)
    return


def draw_months_in_circle(circle_radius, figure_axes):
    # month_names = Table(Time(["2023-{0:02d}-01".format(i) for i in range(1, 13)]).datetime, names=['Month']).to_pandas().Month.dt.strftime('%B').tolist()
    # month_names = Table(data=[Time(["2023-{0:02d}-01".format(i) for i in range(1, 13)]).datetime.strftime('%B')],
    #                names=['Month'])
    month_names = list(month_name)[1:]
    phase_shift = -np.pi/3 - (15/30)*(2*np.pi/12)   # move June to top and shift by 2/3 month to ~20th
    number_of_months = len(month_names)
    for month_index, name in enumerate(month_names):
        month_angle = np.radians(month_index * (360 / number_of_months))
        rotation_angle = np.degrees(month_angle + phase_shift - np.pi / 2)
        if np.abs(rotation_angle) > 90:
            rotation_angle += 180
        figure_axes.text(circle_radius * np.cos(month_angle + phase_shift), circle_radius * np.sin(month_angle + phase_shift),
                  name,
                  ha='center', va='center', rotation=rotation_angle)
    return


def draw_month_name_division_marks():
    return


def draw_solstice_equinox_marks(circle_radius, reduction_factor=0.8):
    # Equinox segment
    plt.plot([-reduction_factor*circle_radius, reduction_factor*circle_radius], [0., 0.], color='black')
    # Solstice segment
    plt.arrow(0, -reduction_factor*circle_radius, 0, 2*reduction_factor*circle_radius,
              color='black', head_width=0.05*circle_radius)
    # Northern solstice
    plt.text(0.05*circle_radius, 0.85*reduction_factor*circle_radius, 'Northern\nSolstice', ha='left', va='center')
    # Northward equinox
    plt.text(0.85 * reduction_factor * circle_radius, -0.05 * reduction_factor * circle_radius, 'Northward\nEquinox',
             ha='center',
             va='top')
    # Southern solstice
    plt.text(0.05 * circle_radius, -0.85 * reduction_factor * circle_radius, 'Southern\nSolstice', ha='left',
             va='center')
    # Southward equinox
    plt.text(-0.85 * reduction_factor * circle_radius, -0.05 * reduction_factor * circle_radius, 'Southward\nEquinox',
             ha='center',
             va='top')
    return


def draw_constellation_symbols():
    return


def draw_constellation_boundary_marks():
    return


def draw_constellation_asterisms():
    return


if __name__ == '__main__':
    # draw_annual_circle()
    draw_annual_circle(file_name='MonthsAndStars.svg')
