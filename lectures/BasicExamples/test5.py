
x=1

lp = 0
while x <= 1000:
 lp=lp+1
 x=x*2
 print("x: " + str(x))
 print("lp: " + str(lp))

#This is called a 'while' loop, the commands will keep iterating as long as x <= 1000 is true (it stops when it is no longer true)
#The <= is a symbol that means less-than-or-equal to.
#A while loop doesn't have a loop variable, so I created a variable 'lp' that keeps track of the number of iterations.