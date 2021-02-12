import numpy as np

# y^2 + a x y + b x ^2 + c y + d x + e = 0
# a' = b/e, b' = 1/e, f' = c/(2e), g' = d/(2e), h' = a/(2e),
alternate_parameters = [-133 / 250, 16 / 25, 0., 0., -64]

# # parameters = [alternate_parameters[1]/alternate_parameters[4],
#               1./alternate_parameters[4],
#               alternate_parameters[2]/alternate_parameters[4],
#               alternate_parameters[3]/alternate_parameters[4],
#               alternate_parameters[0]/alternate_parameters[4]]
#
# print(parameters)
# xvalues = np.linspace(-parameters[0], parameters[0])
# yvalues = np.linspace(-parameters[1], parameters[1])
#
# def five_point_determinant(fit_points, x, y):
#     matrix = np.array([[x**2, x*y, y**2, x, y , 1],
#                        [fit_points[0][0]**2, fit_points[0][0]])

a, b = 10., 8.,
c = np.sqrt(a**2 - b**2)
e = c/a
print('For an ellipse with a = {}, b = {}, then e = {:.1f}, c = {:.1f}'.format(a, b, e, c))
print()

x, y = 6, -5
fit_points = np.array([[0, 8], [10, 0], [0, -8], [-10, 0], [-6, 5]])

column1 = np.append([x], fit_points[:, 0]) ** 2
column2 = np.append([x * y], fit_points[:, 0] * fit_points[:, 1])
column3 = np.append([y], fit_points[:, 1]) ** 2
column4 = np.append([x], fit_points[:, 0])
column5 = np.append([y], fit_points[:, 1])
column6 = np.ones([6])
matrix = np.array([column1, column2, column3, column4, column5, column6]).T

print('det (\n{}\n) \n= {}'.format(matrix, np.linalg.det(matrix)))
print()

# A = det(minor matrix of x^2)
xsquared_minor = np.array([fit_points[:, 0] * fit_points[:, 1],
                           fit_points[:, 1] ** 2,
                           fit_points[:, 0],
                           fit_points[:, 1],
                           np.ones(5)]
                          ).T
A = np.linalg.det(xsquared_minor)
print('A = {}'.format(A))

# B = det(minor matrix of x*y)
xy_minor = np.array([fit_points[:, 1] ** 2,
                     fit_points[:, 0],
                     fit_points[:, 1],
                     np.ones(5),
                     fit_points[:, 0] ** 2]
                    ).T
B = np.linalg.det(xy_minor)
print('B = {}'.format(B))

# C = det(minor matrix of y^2)
ysquared_minor = np.array([fit_points[:, 0],
                           fit_points[:, 1],
                           np.ones(5),
                           fit_points[:, 0] ** 2,
                           fit_points[:, 0] * fit_points[:, 1]]
                          ).T
C = np.linalg.det(ysquared_minor)
print('C = {}'.format(C))

# D = det(minor matrix of x)
# E = det(minor matrix of y)
# F = det(minor matrix of 1)

discriminant = B ** 2 - 4*A*C
print('discriminant = B^2 - 4*A*C = {}'.format(discriminant))
# S_matrix = np.array([[    A, 0.5*B, 0.5*D],
#                      [0.5*B,     C, 0.5*E],
#                      [0.5*D, 0.5*E,     F]])
# eta = np.sign(np.linalg.det(S_matrix))
eta = 1
eccentricity = np.sqrt(2 * np.sqrt((A - C) ** 2 + B ** 2) /
                       (eta * (A + C) + np.sqrt((A - C) ** 2 + B ** 2)))

if discriminant < 0:
    if A != C:
        print('\t Ellipse: e = {}'.format(eccentricity))
    else:
        print('\t Circle: e = 0')
elif discriminant > 0:
    if A != -C:
        print('\t Hyperbola: e = {}'.format(eccentricity))
    else:
        print('\t Rectangular Hyperbola')
else:
    print('\t Parabola: e = 1')

