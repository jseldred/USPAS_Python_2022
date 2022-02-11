#example revisting dispersion matching, this time with an optimizer

import numpy as np
#import minimize if you plan to use it.
from scipy.optimize import minimize

rho = 30
th = np.pi/24.0

#This function takes the parameters as input and returns a quantity to be minimized
#In this case, the fit parameter will control the matrix properties
#There return value will be the magnitude of dispersion at the end.
def DispMatch(fparam):
  #declaring these global variables lets me take them inside the function without making them arguments
  global rho, th
  #doesn't matter if I pass negative values, only positive values will be used.
  f1 = np.abs(fparam[0])
  f2 = np.abs(fparam[1])
  L1 = np.abs(fparam[2])
  L2 = np.abs(fparam[3])
  #Dispersion matrices
  QF = np.matrix([[1, 0, 0], [-1/f1, 1, 0], [0, 0, 1]])
  QD = np.matrix([[1, 0, 0], [-1/f2, 1, 0], [0, 0, 1]])
  O1 = np.matrix([[1, L1, 0], [0, 1, 0], [0, 0, 1]])
  O2 = np.matrix([[1, L2, 0], [0, 1, 0], [0, 0, 1]])
  B = np.matrix([[np.cos(th), rho*np.sin(th), rho*(1-np.cos(th))], [-np.sin(th)/rho, np.cos(th), np.sin(th)], [0, 0, 1]])
  #Achromat has a quad-triplet in the center.
  M=B*O1*QD*O2*QF*O2*QD*O1*B
  #zero dispersion vector
  Din = np.matrix([0,0,1]).T
  #outgoing dispersion vector 
  Dout=M*Din
  #this quantity should be minimizes
  #I don't need to take the sqrt, because that would be minimizing the same thing
  objective = np.sum(np.array(Dout-Din)**2)
  return objective

#this is my best guess for starting values
#in the previous exercise f1=0.5*L1 + 0.25*rho*th, which is about 1.5 if L1 is 1.
#But now instead of L1 we now have L1+L2 for length, so let's make it L1=0.5 and L2=0.5
#there should be a solution for a weak QD, so lets start with double f1 for f2.
param0 = [1.5, 3.0, 0.5, 0.5]
#define upper and lower bounds for each parameter
bnds = ((0.0, 10.0), (0.0, 10.0), (0.2, 5.0), (0.2, 5.0))

#this statement starts the minimization
#uses TNC method of minimizing, not all methods use bounds but this one does.
res = minimize(DispMatch, param0, method='TNC', bounds=bnds, options={'disp': True})
print(res)

#because I used bounds, I don't have any negative values in here, but this is how I would fix it if I did.
#you can only do this safely when you also take the absolute value in the function itself
res.x[0] = np.abs(res.x[0])
res.x[1] = np.abs(res.x[1])
res.x[2] = np.abs(res.x[2])
res.x[3] = np.abs(res.x[3])

#res.fun gives the final value of the objective function
#I'm used .format instead of string so I can round scientific notation.
print('Dispersion was matched to the level of ' + "{:.4e}".format(res.fun))

#res.x gives an array of the parameter values
print('Parameters: f1=' + str(np.round(res.x[0],2)) + ', f2=' + str(np.round(res.x[1],2)) + ', L1=' + str(np.round(res.x[2],2)) + ', L2=' + str(np.round(res.x[3],2)))
