#example scipt comparing optimizations of a strange function

import numpy as np
import matplotlib.pyplot as plt
#import minimize if you plan to use it.
from scipy.optimize import minimize

#setup for plotting
xvals = np.arange(-5,5,0.1)
yvals = np.arange(-5,5,0.1)
X,Y = np.meshgrid(xvals,yvals)

#function parameters
freq = 2*np.pi/3.0
amp = 5.0
quad = 0.1

#Plot of the function we are going to optimize
fxy = 2+quad*(X**2)+quad*(Y**2)-(np.cos(freq*X)+np.cos(freq*Y))
plt.pcolormesh(X,Y,fxy, shading='auto')
plt.colorbar()
plt.show()

#The EggCrate function has many sinesoidal local minimums in x and y
#In this case there is also a broad parabolic shape which minimizes at 0,0
#An overall constant is added so that the minimum is exactly zero.
def EggCrate(fparam):
  global freq, amp, quad
  x = fparam[0]
  y = fparam[1]
  return 2+quad*(x**2)+quad*(y**2)-(np.cos(freq*x)+np.cos(freq*y))

#This callback function will be called every iteration
#I will stack the current values into an array that will be used to track the progress
def callbackF(fparam):
  global traj
  traj = np.vstack((traj,np.array(fparam)))

#initial location will be near a local minimum
param0 = [-3, 4.0]
#upper and lower bounds for each parameter
bnds = ((-8.0, 8.0), (-8.0, 8.0))

#We will compare three methods, TNC, Nelder-Mead, and Powell
#TNC is a Newton gradient-based method
traj = param0
res = minimize(EggCrate, param0, method='TNC', bounds=bnds, callback=callbackF, options={'disp': True})

#Plot trajectory for TNC
fxy = 2+quad*(X**2)+quad*(Y**2)-(np.cos(freq*X)+np.cos(freq*Y))
plt.pcolormesh(X,Y,fxy, shading='auto')
plt.colorbar()
plt.plot(traj[:,0],traj[:,1],color='black',linewidth=0.5)
plt.scatter(traj[:,0],traj[:,1],color='red',s=8)
plt.title('TNC optimization')
plt.savefig('lec5_func_optim_1.png', bbox_inches='tight')
plt.show()

#Nelder-Mead is a simplex method
traj = param0
res = minimize(EggCrate, param0, method='Nelder-Mead', bounds=bnds, callback=callbackF, options={'disp': True})

#Plot trajectory for TNC
fxy = 2+quad*(X**2)+quad*(Y**2)-(np.cos(freq*X)+np.cos(freq*Y))
plt.pcolormesh(X,Y,fxy, shading='auto')
plt.colorbar()
plt.plot(traj[:,0],traj[:,1],color='black',linewidth=0.5)
plt.scatter(traj[:,0],traj[:,1],color='red',s=8)
plt.title('Nelder-Mead optimization')
plt.savefig('lec5_func_optim_2.png', bbox_inches='tight')
plt.show()

#Powell is a conjugate direction method
traj = param0
res = minimize(EggCrate, param0, method='Powell', bounds=bnds, callback=callbackF, options={'disp': True})

#Plot trajectory for Powell
fxy = 2+quad*(X**2)+quad*(Y**2)-(np.cos(freq*X)+np.cos(freq*Y))
plt.pcolormesh(X,Y,fxy, shading='auto')
plt.colorbar()
plt.plot(traj[:,0],traj[:,1],color='black',linewidth=0.5)
plt.scatter(traj[:,0],traj[:,1],color='red',s=8)
plt.title('Powell optimization')
plt.savefig('lec5_func_optim_3.png', bbox_inches='tight')
plt.show()
