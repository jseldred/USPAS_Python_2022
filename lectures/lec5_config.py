#example script showing file input

import numpy as np
import matplotlib.pyplot as plt
import sys

#sys.argv is a list of input arguments for the file
#the first input is 1 (since 0 is the python file name)

##These are the default values of the inputs
#spring constant and particle mass
k = 3.0
m = 0.5
#initial conditions
x0 = 1.0
p0 = 0.0
#timestep config
tstep = 0.01
tmax = 2.0

##This overwrites the default values
#I can specify no parameters, just the first two, just the first four, or all six.
if len(sys.argv) == 3:
  try:
    k = float(sys.argv[1])
    m = float(sys.argv[2])
  except:
    sys.exit('Input format error for 2 inputs.')
elif len(sys.argv) == 5:
  try:
    k = float(sys.argv[1])
    m = float(sys.argv[2])
    x0 = float(sys.argv[3])
    p0 = float(sys.argv[4])
  except:
    sys.exit('Input format error for 4 inputs.')
elif len(sys.argv) == 7:
  try:
    k = float(sys.argv[1])
    m = float(sys.argv[2])
    x0 = float(sys.argv[3])
    p0 = float(sys.argv[4])
    tstep = float(sys.argv[5])
    tmax = float(sys.argv[6])
  except:
    sys.exit('Input format error for 6 inputs.')

##Now we do the simulation

#setup time variable
t = np.arange(0,tmax,tstep)
tnum = len(t)

#setup first point
x = np.zeros(tnum)*np.nan
p = np.zeros(tnum)*np.nan
x[0] = x0
p[0] = p0

#Euler-Cromer Method
for lp in range(1,tnum):
  x[lp] = x[lp-1] +(p[lp-1]/m)*tstep
  p[lp] = p[lp-1] -(k*x[lp])*tstep

#Use consistent scale for q and p (in whatever units)
qmax = np.max(( np.max(x), np.max(p) ))*1.1
qmin = np.min(( np.min(x), np.min(p) ))*1.1

#Plot x vx p
plt.scatter(x,p,s=8,c=np.arange(0,tnum))
plt.xlabel('X')
plt.ylabel('P')
plt.title('Trajectory of the Harmonic Oscillator')
plt.xlim((qmin,qmax))
plt.ylim((qmin,qmax))
plt.show()
