import numpy as np


def calculate_vertex_coordinates(radius, number_of_vertices, density_of_vertices, starting_angle=np.pi/2):
    angles = [starting_angle -
              n * (density_of_vertices/number_of_vertices) * (2. * np.pi) for n in range(number_of_vertices+1)]
    coordinates = radius * np.array([[np.cos(angle), np.sin(angle)] for angle in angles])
    return coordinates
