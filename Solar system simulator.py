import vpython as vp
import numpy as np

sun = vp.sphere(color = vp.color.yellow)
earth = vp.sphere(color = vp.color.green,radius = 1/10)
radius = 5
earth.pos = vp.vector(radius,0,0)
number_of_orbits = 2
number_of_points = 500
period = 1
times = np.linspace(0,period*number_of_orbits,num=number_of_points)
for time in times:
    vp.rate(30)
    x = radius*np.cos(2*np.pi*time/period)
    y = radius*np.sin(2*np.pi*time/period)
    earth.pos = vp.vector(x,y,0)