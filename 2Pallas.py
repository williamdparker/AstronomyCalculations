from astropy.time import Time
from astropy.coordinates import SkyCoord, get_sun
import numpy as np

# Coordinate notation
#   xyz = heliocentric plane of orbit
#       x = r cos v, y = r sin v, z = 0  where r = heliocentric distance, v = true anomaly
#   XYZ = heliocentric ecliptic
#       X = r cos β cos λ, Y = r cos β sin λ, Z = r sin β   where β = ecliptic latitude, λ = ecliptic longitude
#   ξηζ = heliocentric equatorial coordinates
#   x_,y_,z_ = geocentric equatorial coordinates
#       x_ = Δ cos δ cos α, y_ = Δ cos δ sin α, z_ = Δ sin δ    where Δ = geocentric distance, δ = declination, α = RA

# α = right ascension, δ = declination
#   x_ = Δ cos δ cos α = l Δ = x0_ + ξ      where x0_ = geocentric equatorial x-coordinate of the Sun
#   y_ = Δ cos δ sin α = m Δ = y0_ + η      where y0_ = geocentric equatorial y-coordinate of the Sun
#   z_ = Δ sin δ       = n Δ = z0_ + ζ      where z0_ = geocentric equatorial z-coordinate of the Sun
#   l^2 + m^2 + n^2 = 1





# Write a function to convert declination and right ascension into (l, m , n) and check l^2 + m^2 + n^2 = 1
def convert_equatorial_coordinates_to_cartesian_angles(declination, right_ascension):
    l = np.cos(declination) * np.cos(right_ascension)
    m = np.cos(declination) * np.sin(right_ascension)
    n = np.sin(declination)
    # print(f"l^2 + m^2 + n^2 = {l ** 2 + m ** 2 + n ** 2}")
    return l, m, n


# Look at the Astropy coordinates SkyCoord class
#   https://docs.astropy.org/en/stable/coordinates/
# Use Astropy to get position of Sun at times
#   https://docs.astropy.org/en/stable/api/astropy.coordinates.get_sun.html#astropy.coordinates.get_sun
#   GCRS should give us (Δ, δ, α) of Sun ; for practice, you should directly calculate (x0_, y0_, z0_)
#   and then check with the Astropy converter
#   https://docs.astropy.org/en/stable/api/astropy.coordinates.spherical_to_cartesian.html#astropy.coordinates.spherical_to_cartesian

# Write a function called crude_approximation_geocentric
#   that takes (l1, m1, n1), (l3, m3, n3), (x0_1, y0_1, z0_1), (x0_2, y0_2, z0_2), and (x0_3, y0_3, z0_3)
#   and returns (Δ1, Δ2, Δ3) using the equations 13.7.4-13.7.6 and a1 = b1 = 2/3, a3 = b3 = 1/3
def crude_approximation_geocentric(observation_times, geocentric_angles):
    """
    Parameters
    ----------
    observation_times : tuple of 3 astropy Time objects
        Represents 3 observation times.
    geocentric_angles : ndarray(3, 3)
        Geocentric angles, 1 per observation time (radians).
        (l, m, n)
    Returns
    -------
    geocentric_distances : tuple of floats
        Objects distances from earth at 3 observation times.
    """
    earth_sun_separations = []
    for time in observation_times:
        earth_sun_separation = get_sun(time)
        earth_sun_separation.representation_type = 'cartesian'
        earth_sun_separations.append([earth_sun_separation.x.value, earth_sun_separation.y.value,
                                      earth_sun_separation.z.value])
        # print('Appending {} a.u. magnitude separation to earth_sun_separations'.format(np.sqrt(
        #     earth_sun_separation.x.value**2 + earth_sun_separation.y.value**2 + earth_sun_separation.z.value**2)))
    print('XYZ = {}'.format(earth_sun_separations))

    a1 = 2/3
    a3 = 1/3
    geocentric_distance_coefficients = np.zeros((3, 3))

    geocentric_distance_coefficients[:, 0] = a1 * geocentric_angles[0]
    print('GAF[0] ={}'.format(geocentric_angles[0]))
    print()
    geocentric_distance_coefficients[:, 1] = -1 * geocentric_angles[1]
    geocentric_distance_coefficients[:, 2] = a3 * geocentric_angles[2]

    print('GAF = {}'.format(geocentric_angles))
    print()
    print('LHS = {}'.format(geocentric_distance_coefficients))
    print()

    earth_sun_separations = np.array(earth_sun_separations)
    # print(earth_sun_separations)
    earth_sun_separation_coefficients = a1 * earth_sun_separations[0]
    earth_sun_separation_coefficients += -1 * earth_sun_separations[1]
    earth_sun_separation_coefficients += a3 * earth_sun_separations[2]
    print('RHS = {}'.format(earth_sun_separation_coefficients))
    geocentric_distances = np.linalg.solve(geocentric_distance_coefficients, earth_sun_separation_coefficients)

    return geocentric_distances


# Write a function called geocentric_to_heliocentric to get (ξηζ) and r from (lmn), Δ, and (x0_, y0_, z0_)
#   [you might be able to transform from GCRS to HCRS frame using Astropy but it would be good to practice]


# Values in AU from chapter 13.7.1
chi_values = (-3067283, -3861944, -5363308)
eta_values = (0.8892900, 0.8626457, 0.7913872)
zeta_values = (0.3855495, 0.3739996, 0.3431004)

if __name__ == '__main__':
    c = SkyCoord.from_name("Sirius")
    dec = c.dec.radian
    ra = c.ra.radian
    l, m, n = convert_equatorial_coordinates_to_cartesian_angles(dec, ra)
    # convert all example times and coordinates into (l, m, n)
    print(l, m, n)
    print()
    northward_equinox_approximate = Time('2021-03-20T16:45:00', format='isot', scale='utc')

    sun_at_equinox = get_sun(northward_equinox_approximate)
    sun_at_equinox.representation_type = 'cartesian'
    print(float(sun_at_equinox.x.value))

    # Values taken from Chapter 13.6 of Celestial Mechanics (Tatum)
    times = ['2002-07-10', '2002-07-15', '2002-07-25']
    time_objects = []
    for time in times:
        time_objects.append(Time(time+'T00:00:00', format='isot', scale='utc'))

    # Values of angular coordinates in radians
    right_ascensions = [5.5649, 5.5521, 5.5222]
    declinations = [0.2833, 0.2803, 0.2690]

    geocentric_cartesian_angles = []
    for right_ascension, declination in zip(right_ascensions, declinations):
        geocentric_cartesian_angles.append(convert_equatorial_coordinates_to_cartesian_angles(declination,
                                                                                              right_ascension))
    geocentric_cartesian_angles = np.array(geocentric_cartesian_angles)
    geocentric_distances = crude_approximation_geocentric(time_objects, geocentric_cartesian_angles)
    print(geocentric_distances)

    A = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]])
    B = np.array([4, 5, 6])
    print("Solutions:\n", np.linalg.solve(A, B))


    # now convert sun (α, δ, Δ) to (x0_, y0_, z0_) for each time
    # set a1 = 2/3 & b1 = 1/3  (why??)
    # setup system of three linear equations for unknown distances (Δ1, Δ2, Δ3)
    #  Equations 13.7.4 - 13.7.6 in Tatum

    # find vector coefficients (a1, a3) relating r1 & r3 to r2
