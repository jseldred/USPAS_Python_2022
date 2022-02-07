
import numpy as np

x = np.zeros(10)

for lp in range(10):
 x[lp] = lp+1
 print("x: " + str(x))

print("test 7 complete.")
#That was test7.py

for lp1 in range(3):
 for lp2 in range(10):
  x[lp2] = 2*x[lp2]
 print("x: " + str(x))

#lp1 keeps track of the number of x2 operations
#lp2 keeps track of where you are in the array x.