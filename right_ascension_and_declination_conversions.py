import numpy as np

# Values taken at 8:15 p.m. 3-31-2021
right_ascension = '00h 41m 22s'
declination = '+04° 26m 56s'


def right_ascension_hms_string_to_radians_float(ra):
    """Given input RA in format ##h ##m ##s return RA in decimal radians"""
    # Note: we should probably adapt to ##.##s form as well
    hours = float(ra[:2])
    minutes = float(ra[4:6])/60.                                   # 60 m in 1 h
    seconds = float(ra[8:10])/3600.                                # 3600 s in 1 h
    right_ascension_float = (hours + minutes + seconds)*np.pi/12.  # 2π rad in 24 h
    return right_ascension_float


def declination_dms_string_to_radians_float(dec):
    """Given input declination in format +##d ##m ##s return declination in decimal radians"""
    return declination_float


def declination_dms_string_to_radians_float(δ, α):
    """Given input declination and RA in radians, return [l,m,n] angular component of geocentric equatorial
    coordinates """
    l = np.cos(δ) * np.cos(α)
    m = np.cos(δ) * np.sin(α)
    n = np.sin(δ)
    geocentric_coordinates_angular_part = [l, m, n]
    return geocentric_coordinates_angular_part


def test_geocentric_coordinates_angular_part(coordinates):
    sum_of_squares = 0
    for index in len(coordinates):
        sum_of_squares += coordinates[index]**2
    if sum_of_squares == 1.:
        return True
    else:
        print(f"l^2 + m^2 + n^2 = {sum_of_squares} != 1")
        return False


print(right_ascension_hms_string_to_radians_float(right_ascension))


# TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'
## solution: don't place commas at the ends of lines