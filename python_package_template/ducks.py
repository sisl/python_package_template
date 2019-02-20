import math as _math

def ducks_in_earth(duck_volume, R_EARTH=6378e3):
    """Compute the number of ducks that fit in the earth

    Args:
        duck_volume (float): Volume of one rubber duck [m^3]
        R_EARTH (float): Earth's equatorial radius [m] Default: 6,378,000.0

    Returns:
        num_ducks (int): Number of whole ducks that it would take to fill the Earth
    """

    return _math.floor((4/3*_math.pi*R_EARTH**3)/duck_volume)