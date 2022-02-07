
import numpy as np

from test7 import x
import test7

#I can invoke test7.py to run the previous program, instead of typing it again. But first I need to initialize x.

print("test 7 complete.")

sfin = np.zeros(len(x))

#Here, instead of writing out 10 again I used a function that would find the length of x.

lp = 0
lpflag = 0
while lpflag == 0:
 lp = lp+1
 for lp2 in range(len(x)):
  if (sfin[lp2] == 0):
   x[lp2] = 2*x[lp2]
   if x[lp2] > 1000:
    sfin[lp2] = lp
	#once x[lp2] is greater than 1000, the corresponnding sfin value is changed from zero, and x[lp2] doesn't change again.
 
 #The following expression is used to check if there are any values of sfin which are zero. If they are all nonzero, lpflag = 1. If one is zero, lpflag = 0.
 lpflag = 1
 for lp2 in range(len(sfin)):
  if (sfin[lp2] == 0):
   lpflag = 0

#It's okay that I put the line break between two sections of my while loop. They are still all part of the same loop as long as I keep the indentation (including for the line break).

print("x: " + str(x))
print("sfin: " + str(sfin))

#notice that all the values of x are somewhere between 1000 and 2000, because that's where they stopped multiplying.
#notice that the final values of sfin become smaller as the corresponding initial value gets larger.