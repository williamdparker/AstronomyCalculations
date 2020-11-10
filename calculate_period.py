import numpy as np


def calculate_sidereal_period(inferior_period, superior_period):
    if inferior_period > 0. and superior_period > 0.:
        return 1./((1./inferior_period) - (1./superior_period))
    else:
        return 0.


