import numpy as np
import matplotlib.pyplot as plt


# Calculate the x-y pair for a point at a given angle on a circle of some radius
def circle(parameter, radius=1.0):
    return radius*np.cos(parameter), radius*np.sin(parameter)


def ellipse(parameter, semimajor_axis=2.0, semiminor_axis=1.0):
    return semimajor_axis*np.cos(parameter), semiminor_axis*np.sin(parameter)


parameters = np.linspace(0., 2*np.pi, num=500)

if __name__ == '__main__':
    horizontal_coordinates, vertical_coordinates = circle(parameters)
    plt.plot(horizontal_coordinates, vertical_coordinates)

    horizontal_coordinates, vertical_coordinates = ellipse(parameters)
    plt.plot(horizontal_coordinates, vertical_coordinates)

    horizontal_coordinates, vertical_coordinates = ellipse(parameters, semimajor_axis=3.0)
    plt.plot(horizontal_coordinates, vertical_coordinates)

    plt.axes().set_aspect('equal')
    plt.show()
