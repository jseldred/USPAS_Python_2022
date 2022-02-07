#This is an alternate solution to problem 5

x=1

lp = 0
lpflag=0
while lpflag = 0:
 lp=lp+1
 x=x*2
 print("x: " + str(x))
 print("lp: " + str(lp))
 if (x > 1000):
  lpflag = 1

#here we put an 'if statement' within a while loop.
#The indented line after the 'if statement' will run if the 'if statement' is true. That lpflag variable will stop the looping.
#technically this code has a flaw if it takes more then 200 iterations for x > 1000, but since that would never happen its okay.