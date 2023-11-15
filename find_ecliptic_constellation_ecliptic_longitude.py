from astropy.coordinates import SkyCoord
from astropy.coordinates import GeocentricTrueEcliptic
import numpy as np
import matplotlib.pyplot as plt
from astronomical_symbols import astronomical_symbols


#
# MODIFY TO USE GeocentricTrueEcliptic COORDINATES FROM THE START
#

obliquity = 23.43656  # deg
number_of_samples = 360*60*60  # 1 sample per arcsecond

sample_spacing = 360. / number_of_samples
ecliptic_RAs = np.linspace(0., 360. - sample_spacing, num=number_of_samples)
ecliptic_decs = obliquity*np.sin(2.*np.pi*ecliptic_RAs/360.)
ecliptic_coordinates = SkyCoord(ecliptic_RAs, ecliptic_decs, unit="deg")
ecliptic_constellations = ecliptic_coordinates.get_constellation()

boundary_coordinate_indices = np.where(ecliptic_constellations[:-1] != ecliptic_constellations[1:])[0]

boundary_coordinates = np.empty(shape=(len(boundary_coordinate_indices), 2), dtype=float)
boundary_constellation_names = []

index = 0
for boundary_coordinate_index in boundary_coordinate_indices:
    boundary_coordinates[index] = ecliptic_RAs[boundary_coordinate_index], ecliptic_decs[boundary_coordinate_index]
    if ecliptic_constellations[boundary_coordinate_index] != 'Ophiucus':
        boundary_constellation_names.append(ecliptic_constellations[boundary_coordinate_index])
    else:
        boundary_constellation_names.append('Ophiuchus')
    index += 1

index = 0
for constellation in boundary_constellation_names:
    current_coordinate = SkyCoord(boundary_coordinates[index][0], boundary_coordinates[index][1], unit='deg')
    print(constellation)
    print(current_coordinate.transform_to(GeocentricTrueEcliptic))
    # print(current_coordinate.CoordinateTransform(GCRS, GeocentricTrueEcliptic))
#    print('{}: ({})\n'.format(astronomical_symbols[constellation], boundary_coordinates[index]))
    index += 1

# print(boundary_coordinates)


#plt.plot(ecliptic_RAs, ecliptic_decs)
#plt.show()