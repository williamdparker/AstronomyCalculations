from draw_sun_arcs import draw_sun_arcs
from draw_week_heptagram import draw_week_heptagram
from draw_lunar_cycle import draw_lunar_cycle
from draw_annual_circle import draw_annual_circle

from matplotlib import pyplot as plt


# draw figure border
#
# sun arc day figure
## put observatory icon at south
## add tree icons on horizon if not too cluttered

if __name__ == '__main__':
    plt.style.use('calendar_sign.mplstyle')
    draw_sun_arcs()
    draw_lunar_cycle()
    draw_week_heptagram()
    draw_annual_circle()

