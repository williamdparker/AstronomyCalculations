from calculate_regular_star_polygram_vertices import calculate_vertex_coordinates
from astronomical_symbols import astronomical_symbols
import matplotlib.pyplot as plt

# Plot parameters
radius = 1.
polygram_line_color = 'green'
symbol_placement_factor = 1.1
symbol_fontsize = 16
day_placement_factor = 1.25
day_fontsize = 14

# Heptagram data
polygram_objects = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn']
number_of_vertices = len(polygram_objects)
vertex_offset = 3
polygram_vertex_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


polygram_coordinates = calculate_vertex_coordinates(radius, number_of_vertices, vertex_offset)
plt.plot(polygram_coordinates[:, 0], polygram_coordinates[:, 1], color=polygram_line_color)

polygram_symbols = []
for sky_object in polygram_objects:
    polygram_symbols.append(astronomical_symbols[sky_object])

polygram_symbol_coordinates = symbol_placement_factor * polygram_coordinates

polygram_day_coordinates = day_placement_factor * polygram_coordinates

symbol_index = 0
for symbol in polygram_symbols:
    plt.text(polygram_symbol_coordinates[symbol_index][0], polygram_symbol_coordinates[symbol_index][1], symbol,
             ha='center', va='center', fontsize=symbol_fontsize)
    plt.text(polygram_day_coordinates[symbol_index][0], polygram_day_coordinates[symbol_index][1],
             polygram_vertex_days[symbol_index], ha='center', va='center', fontsize=day_fontsize)
    symbol_index += 1

plt.axis('off')

plt.show()
