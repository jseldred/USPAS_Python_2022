#example of a script that calculates a phase-space vectors for a harmonic oscillator

import numpy as np
import matplotlib.pyplot as plt

#spring constant and particle mass
k = 3.0
m = 0.5

#setup x grid and y grid
x_list = np.linspace(-2.1,2.1,20)
p_list = np.linspace(-2.1,2.1,20)

#put values of x and p as a 2D array
x, p = np.meshgrid(x_list, p_list)
#Hamiltonian
H = 0.5*k*(x**2) + 0.5*(p**2)/m
#Calculate change in x and p with time
dxdt = p/m
dpdt = -k*x
#phase-space velocity
v = np.sqrt(dxdt**2 + dpdt**2)

#Quiver plot: x-coordinate, y-coordinate,
#x-projection of arrow, y-projection of arrow,
#color (usually length of arrow)
plt.quiver(x,p,dxdt,dpdt,v)
plt.xlim((-2,2))
plt.ylim((-2,2))
plt.xlabel('x')
plt.ylabel('p')
plt.title('Phase-space vectors for the Harmonic Oscillator')
plt.savefig('lec2_quiver.png', bbox_inches='tight')
plt.show()
