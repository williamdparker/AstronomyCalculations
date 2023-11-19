from calculate_regular_star_polygram_vertices import calculate_vertex_coordinates
from astronomical_symbols import astronomical_symbols
import matplotlib.pyplot as plt


def draw_week_heptagram(file_name=''):
    # Create plot
    figure, axes = plt.subplots(figsize=(12, 6))

    # Plot parameters
    radius = 1
    polygram_line_color = 'green'
    symbol_placement_factor = 1.1
    symbol_fontsize = 24
    day_placement_factor = 1.30
    day_fontsize = 16

    # Heptagram data
    polygram_objects = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn']
    number_of_vertices = len(polygram_objects)
    vertex_offset = 3
    polygram_vertex_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


    polygram_coordinates = calculate_vertex_coordinates(radius, number_of_vertices, vertex_offset)
    plt.plot(polygram_coordinates[:, 0], polygram_coordinates[:, 1], color=polygram_line_color)

    polygram_symbols = []
    for sky_object in polygram_objects:
        polygram_symbols.append(astronomical_symbols[sky_object])

    polygram_symbol_coordinates = symbol_placement_factor * polygram_coordinates

    polygram_day_coordinates = day_placement_factor * polygram_coordinates

    for symbol_index, symbol in enumerate(polygram_symbols):
        plt.text(polygram_symbol_coordinates[symbol_index][0], polygram_symbol_coordinates[symbol_index][1], symbol,
                 ha='center', va='center', fontsize=symbol_fontsize)
        if symbol_index == 3 or  symbol_index == 4:
            polygram_day_coordinates[symbol_index][1] -= 0.07 * radius
        if symbol_index == 2 or  symbol_index == 5:
            polygram_day_coordinates[symbol_index][1] += 0.03 * radius
        plt.text(polygram_day_coordinates[symbol_index][0], polygram_day_coordinates[symbol_index][1],
                 polygram_vertex_days[symbol_index], ha='center', va='center', fontsize=day_fontsize)

    # Turn off axes
    plt.axis('off')
    # Make ratio equal
    axes.set_aspect('equal')
    # Set x limits
    plt.xlim([-1.5*radius, 4.5*radius])

    # Draw a box
    plt.plot([2.5*radius, 4.0*radius, 4.0*radius, 2.5*radius, 2.5*radius],
             [-1.0*radius, -1.0*radius, 1.0*radius, 1.0*radius, -1.0*radius],
             color='black')

    # Label symbols in box
    text_height = 1.75*radius
    left_x = 2.75*radius
    starting_y = 0.75*radius
    for index, (symbol, label) in enumerate(zip(polygram_symbols, polygram_objects)):
        plt.text(left_x, starting_y - index * text_height/number_of_vertices,
                 symbol + ' ' + label, color='black', fontsize=day_fontsize,
                 ha='left', va='center')

    if len(file_name) == 0:
        plt.show()
    else:
        plt.savefig(file_name)


if __name__ == '__main__':
    draw_week_heptagram()
    # draw_week_heptagram(file_name='WeekHeptagram.svg')