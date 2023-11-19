from astroquery.vizier import Vizier
from astropy.coordinates import SkyCoord
import astropy.units as u

def get_brightest_stars_coordinates(constellation, num_stars=5):
    """
    Get the right ascensions and declinations of the brightest stars in a given constellation.

    Parameters:
    - constellation: str, the name of the constellation.
    - num_stars: int, the number of brightest stars to retrieve.

    Returns:
    - List of dictionaries containing 'name', 'ra', and 'dec' keys for each star.
    """
    # Query the Bright Star Catalog using Vizier
    vizier = Vizier(columns=["*", "+_r"], catalog="V/50")
    result = vizier.query_region(constellation, radius=1 * u.deg, catalog=["V/50"])

    if result is None or len(result) == 0:
        raise ValueError("Constellation not found in the Bright Star Catalog.")

    # Sort stars by brightness
    brightest_stars = sorted(result[0], key=lambda star: star['Vmag'])[:num_stars]

    # Format result as a list of dictionaries
    # result_list = [{'name': star['Main_ID'], 'ra': star['RAJ2000'], 'dec': star['DEJ2000']} for star in brightest_stars]

    return brightest_stars

# Example usage:
constellation_name = "Orion"
brightest_stars = get_brightest_stars_coordinates(constellation_name, num_stars=10)

print("Brightest Stars in", constellation_name)
for star in brightest_stars:
    print(star)
    # print(f"{star[2]:10} RA: {star[6]}", f"Dec {star[7]}")
