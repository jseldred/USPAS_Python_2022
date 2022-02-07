#This is an alternate solution to problem 5

import sys

#this command imports a python package called 'sys', which allows us to use extra commands.

x=1

for lp in range(200):
 x=x*2
 print("x: " + str(x))
 print("lp: " + str(lp+1))
 if (x > 1000):
  sys.exit()

#here we put an 'if statement' within a for loop.
#this solution is like test5b.py, except it uses a special command 'sys.exit()' to exit the program before the loop can be completed.

#always keep track of whether you want you loop variables to start at 1 or 0, in this case I just add one.