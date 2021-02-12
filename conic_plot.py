# y^2 + a x y + b x ^2 + c y + d x + e = 0
# a' = b/e, b' = 1/e, f' = c/(2e), g' = d/(2e), h' = a/(2e),
alternate_parameters = [-133/250, 16/25, 0., 0., -64]
import numpy as np
# # parameters = [alternate_parameters[1]/alternate_parameters[4],
#               1./alternate_parameters[4],
#               alternate_parameters[2]/alternate_parameters[4],
#               alternate_parameters[3]/alternate_parameters[4],
#               alternate_parameters[0]/alternate_parameters[4]]

# print(parameters)
#xvalues = np.linspace(-parameters[0], parameters[0])
#yvalues = np.linspace(-parameters[1], parameters[1])

# def five_point_determinant(fit_points, x, y):
#     matrix = np.array([[x**2, x*y, y**2, x, y , 1],
#                        [fit_points[0][0]**2, fit_points[0][0]])

x, y = 6, -5
fit_points = np.array([[0, 8], [10, 0], [0, -8], [-10, 0], [-6, 5]])

column1 = np.append([x], fit_points[:, 0]).reshape([6, 1])**2
column2 = np.append([x*y], fit_points[:, 0]*fit_points[:, 1]).reshape([6, 1])
column3 = np.append([y], fit_points[:, 1]).reshape([6, 1])**2
column4 = np.append([x], fit_points[:, 0]).reshape([6, 1])
column5 = np.append([y], fit_points[:, 1]).reshape([6, 1])
column6 = np.ones([5, 1])

print(column1, column2, column3, column4, column5, column6)
# column34 = np.array([[x, y],
#                      fit_points])
# column123 = np.array([[x**2, x*y, y**2],
#                        fit_points[0]**2, fit_points[0]*fit_points[1]**2])

