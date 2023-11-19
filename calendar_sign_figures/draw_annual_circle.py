from calendar import month_name
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
# import matplotlib


def draw_annual_circle(file_name=''):
    # matplotlib.use('macosx')
    plt.style.use('calendar_sign.mplstyle')
    figure, axes = plt.subplots(figsize=(10, 10))
    radius = 1
    axes.set_xlim(-2 * radius, 2 * radius)
    axes.set_ylim(-2 * radius, 2 * radius)
    calendar_circle = Circle((0, 0), 0.95*radius, edgecolor='black', facecolor='None')
    axes.add_patch(calendar_circle)
    draw_months_in_circle(radius, axes)
    draw_solstice_equinox_marks(radius)

    asterisms_dictionary = get_asterism_coordinates()
    draw_constellation_asterisms(asterisms_dictionary)

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


def get_asterism_coordinates():
    from asterisms import asterisms
    from astropy.coordinates import SkyCoord
    for constellation in asterisms.keys():
        right_ascensions, declinations = [], []
        for star_names in asterisms[constellation].values():
            for star in star_names:
                star_coordinates = SkyCoord.from_name(star)
                right_ascensions.append(star_coordinates.ra.value)
                declinations.append(star_coordinates.dec.value)
        asterisms[constellation]['coordinates'] = np.array([[right_ascensions, declinations]])
    return asterisms


def draw_constellation_asterisms(asterisms):
    equator_radius = 1.5
    declination_scale = (0.75 * equator_radius) / 90
    phase_shift = 0
    vertical_shift = -0.2 * equator_radius

    ecliptic_coordinates = draw_ecliptic(equator_radius, declination_scale, [phase_shift, vertical_shift])

    for constellation in asterisms.keys():
        for coordinates in asterisms[constellation]['coordinates']:
            right_ascensions, declinations = coordinates[0], coordinates[1]

            x_values = (equator_radius + declinations * declination_scale) * \
                       np.cos(right_ascensions * 2 * np.pi / 360 - phase_shift)
            y_values = (equator_radius + declinations * declination_scale) * \
                       np.sin(right_ascensions * 2 * np.pi / 360 - phase_shift) + vertical_shift

            curve, = plt.plot(x_values, y_values)
            plt.scatter(x_values, y_values, color=curve.get_color())

            # Label the graph
            minimum_right_ascension = np.min(right_ascensions)
            minimum_declination = np.min(declinations)
            right_ascension_range = np.max(right_ascensions) - minimum_right_ascension
            # declination_range = np.max(declinations) - minimum_declination

            label_shift = 0.25*equator_radius
            label_right_ascension = minimum_right_ascension + 0.5 * right_ascension_range
            label_declination = 23.44 * np.sin(np.radians(label_right_ascension) - phase_shift) * \
                           declination_scale + label_shift
            if label_declination > 0:
                label_radius = equator_radius + label_declination
            else:
                label_radius = equator_radius

            label_x_position = label_radius * \
                         np.cos((minimum_right_ascension + 0.5 * right_ascension_range) * 2 * np.pi / 360 - phase_shift)

            label_y_position = label_radius * \
                         np.sin((minimum_right_ascension + 0.5 * right_ascension_range) * 2 * np.pi / 360 - phase_shift) \
                         + vertical_shift

            text_rotation = (minimum_right_ascension + 0.5 * right_ascension_range) - 90 - 180 * phase_shift / np.pi
            if text_rotation > 90:
                text_rotation += 180
            if constellation == 'Pisces':
                label_x_position *= -1
                label_y_position += 0.25*equator_radius
                text_rotation = -90


            plt.text(label_x_position, label_y_position, constellation,
                     color=curve.get_color(), ha='center', va='center',
                     rotation=text_rotation,
                    )


    return


def draw_ecliptic(radius, scale, shifts):
    earth_obliquity = 23.44
    right_ascensions = np.linspace(0, 2*np.pi)
    declinations = earth_obliquity * np.sin(right_ascensions)
    x_values = (radius + declinations * scale) * \
               np.cos(right_ascensions - shifts[0])
    y_values = (radius + declinations * scale) * \
               np.sin(right_ascensions - shifts[0]) + shifts[1]

    plt.plot(x_values, y_values, color='black', alpha=0.3)
    annotation_index = 7
    annotation_radius = radius + declinations[annotation_index]*scale
    annotation_angle = right_ascensions[annotation_index] - shifts[0]
    annotation_x = annotation_radius * np.cos(annotation_angle)
    annotation_y = annotation_radius * np.sin(annotation_angle) + shifts[1]
    plt.annotate('Sun\'s Path' + '\n' + '(Ecliptic)',
                 xy=(annotation_x, annotation_y),
                 xytext=(annotation_x + 0.2*radius, annotation_y + 0.2 * radius),
                 arrowprops=dict(facecolor='black', headwidth=7, width=1.0, alpha=0.3),
                 alpha=0.5)
    return np.array([right_ascensions, declinations])

if __name__ == '__main__':
    # draw_annual_circle()
    draw_annual_circle(file_name='MonthsAndStars.svg')
