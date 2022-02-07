
import numpy as np

x = np.zeros(10)

for lp in range(10):
 x[lp] = lp+1
 print("x: " + str(x))

#x[0] would be the first value of the array, x[1] would be the second, so on and so on.
#because lp is a positive integer between 0 and 9 its okay to use it as a loop variable. If I said x[2.5] or x[11], it would cause an error.
#Since lp starts at zero, I have to add one to represent the number of iterations

#numpy arrays can also be converted to strings or printed directly.
#The way I set up the program, the whole array is outputed - usually its simpler just to output the value I changed.
