#example script showing file input

import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

#sys.argv is a list of input arguments for the file
#the first input is 1 (since 0 is the python file name)

#I can use the default parameters on this script with no arguments
#or I can specify parameters from the configuration file by one arguments
#or I can specify parameters from the command line with two input, four, or six.

#spring constant and object mass
k = 3.0
m = 0.5
#initial coordinates
x0 = 1.0
p0 = 0.0
#timestep parameters
tstep = 0.01
tmax = 2.0

#this is the default name of the configuration file
fname = 'lec5_config.txt'

#if there is only one input assume it is the string for a configuration file
if len(sys.argv) == 2:
  #use this filename instead of default filename
  fname = str(sys.argv[1])
  with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
      if len(row) > 0 and str(row[0]).replace('.','',1).isnumeric():
        k = float(row[0])
        m = float(row[1])
        x0 = float(row[2])
        p0 = float(row[3])
        tstep = float(row[4])
        tmax = float(row[5])

#these will overwrite the default values I read from my configuration file
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
