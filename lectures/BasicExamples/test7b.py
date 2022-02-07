#This is an alternate solution to problem 7

import numpy as np

x = np.zeros(10)

for lp in range(len(x)):
 x[lp] = lp+1
 print("x: " + str(x))

#Here, instead of writing out 10 again I used a function that would find the length of x.
#The advantage is that if I change the length of x at one point of the program, I don't then have to change the length of my loop.