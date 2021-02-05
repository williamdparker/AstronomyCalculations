import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt


def power(x, a, b):
    return a*np.power(x, b)


# Planetary orbital periods (in Earth days)
periods = np.array([88.0, 224.7, 365.2, 687.0, 4331, 10747, 30589, 59800])
periods *= 24 * 60 * 60   # convert periods to seconds

# Planetary average orbital distances (in 10^6 km)
distances = np.array([57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4444.5])
distances *= 1.0e9  # convert distances to meters

# Fit the data to a power law
initial_parameters = [1., 1]
parameters, covariance_matrix = opt.curve_fit(f=power, xdata=periods, ydata=distances, p0=initial_parameters)
standard_deviations = np.sqrt(np.diag(covariance_matrix))

print("Fit power function: ({:.0f} +/- {:.0f}) * x^({:.3f} +/- {:.3f})".format(
    parameters[0], standard_deviations[0], parameters[1], standard_deviations[1])
)

# Make the figure
fig = plt.figure()

# Plot data as scatter
plt.scatter(periods, distances)

# Plot fit curve on 1000 points from 0 to 10% above the maximum period
fit_curve_periods = np.linspace(0., 1.1*np.max(periods), num=1000)
plt.plot(fit_curve_periods, power(fit_curve_periods, parameters[0], parameters[1]), linestyle='-.')

# Calculate and plot theoretically expected values for circular orbits and uniform motion
expected_power = 2./3.  # (G m M / r^2) = m r (2 pi / T)^2 --> r = (G M / (2 pi)^2)^(1/3) T^(2/3)
solar_standard_gravitational_parameter = 1.327124400e20  # m^3 s^-2
expected_coefficient = (solar_standard_gravitational_parameter / (2.*np.pi)**2)**(1/3)
print("Expected power function: {:.0f} * x^{:.3f}".format(expected_coefficient, expected_power))
plt.plot(fit_curve_periods, power(fit_curve_periods, expected_coefficient, expected_power), linestyle='--')

# Change the scale to log-log
plt.yscale('log')
plt.xscale('log')

# Label axes
plt.xlabel('Period (s)')
plt.ylabel('Distance (m)')

# Show the plot
plt.show()







