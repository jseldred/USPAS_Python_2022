#Several basic examples of building arrays, matrices, and indexing

import numpy as np

####Appending Lists
#how to use append to build up a list
#start with an empty list
x = []
#lets fill it with prime numbers
for lp in range(1,30):
    prime_flag = 1
    lp2 = 2
    while (lp2 < lp and prime_flag == 1):
        if (lp/lp2 == int(lp/lp2)):
            prime_flag = 0
        lp2 = lp2 + 1
    if (prime_flag == 1):
        #append ads lp to the end of x
        x.append(lp)
        print(len(x))

print(x)

####Stacking Arrays
#Now I cast it as a np.array so I can manipulate it.
x = np.array(x)
#Since x is a numpy array now, .append no longer works
#So instead I have to do hstack
x = np.hstack((x,31))
print(x)
#hstack can also be used to append larger sequences
print(np.hstack((x,[37,41,43])))
#but unlike hstasck, you have to set x equal to if you want it to stick
print(x)

#hstack sticks arrays together horizontally
#vstack is the same used for building 2D arrays
y=2*x
z=3*x
M = np.vstack((x,y))
M = np.vstack((M,z))
print(M)

#one can also define 1D and 2D arrays explicitly
x = np.array([1,2,3,4,5])
M = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(x)
print(M)

####Indexing 2D arrays
#Indexing works as before, except with row, column
#print first row
print(M[0,:])
#print first column
print(M[:,0])
#this is incredibly useful when you forget what order you put your indices

#Some useful functions for understanding the size and shape of a matrix
#total number of elements
print(np.size(M))
#Number of elements along first index
print(np.size(M,0))
#Number of elements along second index
print(np.size(M,1))
#Number of elements in each index
print(M.shape)

####Multi-element Operations
#instead of indexing each element individually,
#one can apply functions to the whole array
#slow way
for lp in range(len(x)):
  print(np.sin(x[lp]))

#fast way
print(np.sin(x))

#By default almost numpy functions operate on an element-wise basis,
#this allows for shorter code that is computationally faster
print(x)
print(x+2)
print(10*x+np.sin(x))
#also for 2D arrays
print(M)
print(M**2)

#numpy also has functions that obtains one number from all the elements
print(x)
print(np.sum(x))
print(np.mean(x))
print(np.max(x))
print(np.min(x))
print(np.std(x))

#Those same operation can be used on 2D arrays
#be default it applies an operation to the entire array
print(M)
print(np.mean(M))
#however, you can also apply it to just one index
print(np.mean(M,0))
print(np.mean(M,1))

####Multi-element Inequalities
#you can also apply an inequality statement and output a boolean to those values for which it applies
cx = np.cos(x)
print(cx)
print(cx > 0)
#number of element of cos(x) which are positive
print(np.sum(cx > 0))
#you can also use this boolean numpy array as an index, to pull out those numbers for which it applies
print(cx[(cx > 0)])
#and finally you can apply a specific operation to just those elements
cx[(cx > 0)] = np.nan
print(cx)

####NaN: Not a Number
#by the way nan is "not a number" which is used to eliminate elements of an array (rather than zero)
#you can pick them out with isnan
np.isnan(cx)
#most arithmetic operations don't work on nan
print(np.nan + 5)
print(np.nan > 0)
print(np.nan <= 0)
print(np.mean(cx))
#sometimes there are special functions which skip the nansd
print(np.nanmean(cx))

####Matrices
#Note that a 2D array is not a matrix.
#When I multiply M by itself in a 2D array, I get element-by-element multiplication
#but that is not how you do matrix multiplication!
M = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(M)
print(M*M)
print(M)
#you can use np.dot to force it to do matrix multiplication
print(np.dot(M,M))
#or you can cast this 2D array as a numpy matrix, which will default to matrix multiplication
M = np.matrix(M)
print(M*M)

#the same rules apply for treating 1D arrays as a vector
v1 = np.array([1,2,3])
v2 = np.array([1,4,7])
print(v1*v2)
#dot product of vectors defaults to the 1x1 'inner product' not the nxn 'outer product'
print(np.dot(v1,v2))
print(np.dot(v2,v1))
#1D arrays have no sense of orientation
print(v1)
print(v1.T)
#however numpy will treat 1D arrays as a vector if we cast them as a matrix
#what is a vector but a matrix with a dimension of 1xn
v1 = np.matrix(v1)
v2 = np.matrix(v2)
print(v2)
print(v2.T)
print(v1*(v2.T))
print((v1.T)*v2)
print(M*(v1.T))
