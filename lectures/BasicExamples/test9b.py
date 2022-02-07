#This is an alternate solution to problem 9

import numpy as np

from test7 import x
import test7

print("test 7 complete.")

sfin = np.zeros(len(x))

lp1 = 0
lpflag = 0
while lpflag == 0:
 lp1 = lp1+1
 for lp2 in range(len(x)):
  if (sfin[lp2] == 0):
   x[lp2] = 2*x[lp2]
   if x[lp2] > 1000:
    sfin[lp2] = lp1
 
 #The following expression is used to check if there are any values of sfin which are zero. This time in one line.
 lpflag = np.min(sfin)
 #np.min finds the minimum value in the numpy array sfin, lpflag = 0 if there is at least on zero value of sfin. Otherwise lpflag > 0.

print("x: " + str(x))
print("sfin: " + str(sfin))


