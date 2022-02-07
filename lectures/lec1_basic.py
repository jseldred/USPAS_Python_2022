#demonstration of the some basic Python operatings

####Variables
#no need to declare variables, they will automatically come into existence with the corresponding data type.
#this is a float, integer, string, respectively
x = 1
y = 2.0
z = 'cat'
b = True

#you can output the value of things, and it will keep the format 
print(y)
print(x)

#if you need to delete a variable for space you can use del, but usually its better to just keep everything around.
del b

#Here equal sign means 'take the value of the thing on the right, set the variable on the left to that value'
x = x + 3
print(x)
y = x
print(y)
print(x)

#when you use plus with a string, it concatenates
w = z + ' in a hat'
print(w)
#you can include numbers if you use str
p = 3.14159265
out = 'The value of pi is approximately ' + str(p)
print(out)
#but you may want to round the numbers before you do so.
#the first argument of round is the number to be rounded, the second is the number of digits to round it to
out = 'The value of pi is approximately ' + str(round(p,2))
print(out)
#you can also take numerical characters and use them as numbers
s = '10'
s = int(s) + 1
print(s)

####Lists
#you can define lists
x = [2, 4, 6, 8, -3, 22]
#when I set x to a new value, the old value was forgotten
#you refer to an element of array with an index that starts at zero
print(x[0])
#len gives the length of the list
print(len(x))
#the index of the last element is one less than that
print(x[5])
#you can also use a variable as an index, if it is an integer
y = 3
print(x[y])
#referring to a range of values, start at the index of the first number end at index before the last one
print(x)
print(x[1:4])
#leaving no first number is equivalent to using 0, the first element
print(x[0:2])
print(x[:2])
#leaving no second number is equivalent to using len(x)
print(x[3:len(x)])
print(x[3:])
#you can use a third number to specify a step size
print(x[0:5:2])
#you can use -1 to specify last element
#you can use -2 to specify next to last element and so on
print(x[-1])
print(x[-2])

####Numpy arrays
#It would be nice to treat a list like a vector, but arithmetic operations do not work on lists
#For instances, if I do 2*x the result is surprising
print(x*2)
#if I were to do x+3, it would throw an error.
#so we can use numpy arrays for this.
#first we import the numpy package
import numpy as np
# the 'as np' part means that we can refer to numpy with the abbreviation np.
#now we cast x as a numpy array
x = np.array(x)
#now arithmetic operations will work as expected
print(x)
print(2*x)
print(x+3)
#we'll come back to numpy arrays

####If Statements
#if statements are followed by a colon
#the conditionally executed statements use an indent
if (2>1):
    print('Yes, 2>1')

#the size of the indent doesn't matter, tab or spaces, so long as you don't change it
#you don't have to use parentheses either
#>= greater than equal
#== exactly equal to (note, don't use '=' for if statements)
#!= not equal to
x=3
y=2
if x>=y:
  print('Yes, 3>=2')

z=2.0
if (y==z):
  print('Yes, 2 is exactly 2')

# and there is of course there is booleans
#'and' is and, 'or' is or, 'not' is not
if (x>=y) and (y==z):
  print('Yes both')

if not (x<y):
  print('Yes, 3 is not less than 2')

#There is also else and elif (else if)
if (4<2):
  print('Surprisingly, 4 < 2?')
elif (3<2):
  print('Actually, 3 < 2?')
else:
  print('Truthfully, both 3 and 4 are greater than 2.')

#a value of 1 is equivalent to a boolean true value
x = 1.0
if x:
  print('Yes')

####For Statements
#the classic formulation is a loop variable counting up from 0 to some number
#identation is also used to identify whether it is part of the loop
for lp in range(10):
  print(lp)

#Here lp is the loop variable (I usually avoid i and j because of complex numbers)
#just like array indexing, starts with 0 and goes to 9.
x = [2, 4, 6, 8, -3, 22]
for lp in range(len(x)):
  print(x[lp])

#actually, you can use any list or array as a sequence for the loop variable
for xlp in x:
  print(xlp)

#you can use numpy to all define custom ranges and iterators
#we already imported numpy, so we don't have to do it again
print(np.arange(2,10,3))
for lp in np.arange(2,10,3):
  print(lp)

#notice arange has the same format as list iterators 2:10:3
#we can nest loops and ifs, so long as we keep track of the indents
for lp in range(10):
  for lp2 in range(4):
    if (lp == lp2):
      print('lp and lp2 value is ' + str(lp))
  print('lp value is ' + str(lp))

####While Statements
#while statements continue to loop as long as the statement is true
#to avoid having the loop occur infinitely, its useful to define a loop variable and manually iterate it
lp=0
while (lp < 10):
  print(lp)
  lp += 1

#another comment technique is to use a loop flag, which breaks the loop
lpflag = 1
lp = 0
while (lpflag and lp < 1000):
  print(lp)
  if (lp == 4):
    print('Found the 4!')
    lpflag = 0
  lp += 1

#another variation is to use a break statement
lp = 0
while (lp<1000):
  print(lp)
  if (lp == 4):
    print('Found the 4!')
    break
  lp += 1

#a while statement will do not run if it is not true to begin with
while (2 < 1):
  print('Surprising!')

####Functions
#here is a function that does a thing, but does not return any values
def sayhello():
  print('Hello!')

#and here I call that function
sayhello()

#here is a function that returns a value
def SetToFour():
  return 4

#here is some examples of using that function
print(SetToFour())
x = SetToFour()
print(x)

#here is a function that takes an argument and returns a value
def AddFour(fx):
  fx = fx + 4.0
  return fx

#an example using that function
x = 3
print(AddFour(x))
print(AddFour(x))
x = AddFour(x)
x = AddFour(x)
print(x)

#once a function is defined, it can be called anywhere in the script
sayhello()

#when the commands run out, the program ends automatically
print('Goodbye!')

