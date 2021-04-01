from astropy.time import Time

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

# Values taken from Chapter 13.6 of Celestial Mechanics (Tatum)
times = ('2002-06-10', '2002-07-15', '2002-07-25'),

# Values in radians
right_ascension = (5.5649, 5.5521, 5.5222)
declination = (0.2833, 0.2803, 0.2690)

# Write a function to convert declination and right ascension into (l, m , n) and check l^2 + m^2 + n^2 = 1

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

# Write a function called geocentric_to_heliocentric to get (ξηζ) and r from (lmn), Δ, and (x0_, y0_, z0_)
#   [you might be able to transform from GCRS to HCRS frame using Astropy but it would be good to practice]


# Values in AU from chapter 13.7.1
chi_values = (-3067283, -3861944, -5363308)
eta_values = (0.8892900, 0.8626457, 0.7913872)
zeta_values = (0.3855495, 0.3739996, 0.3431004)


