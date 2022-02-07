#This is an alternate solution to problem 7

import numpy as np

for lp in range(10):
 x = np.hstack( (np.arange(1,lp),np.zeros(9-lp)) )
 print("x: " + str(x))

#np.arange is a function that creates a numpy array that counts up
#np.hstack is a function that combines to arrays horizontally (appending the second to the first)
#x is recreated in it's entirety each iteration.

