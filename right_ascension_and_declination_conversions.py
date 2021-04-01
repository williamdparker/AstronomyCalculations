import numpy as np

# Values taken at 8:15 p.m. 3-31-2021
right_ascension = '00h 41m 22s'
declination = '+04° 26m 56m'

# α = right ascension, δ = declination in radians
δ = 0.0120
α = 0.0776

x = np.cos(δ) * np.cos(α),
y = np.cos(δ) * np.sin(α),
z = np.sin(δ),

l = x,
m = y,
n = z,

test = l**2 + m**2 + n**2

print(test)

# TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'