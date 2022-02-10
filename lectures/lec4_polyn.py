#basic examples of sympy by manipulating polynomials

import numpy as np
from sympy import *
import matplotlib.pyplot as plt

####Intro to Variables
from sympy.abc import x
#For one-letter symbolic variables, this another way to declare them
#Functionally equivalent to x = symbols('x')

#we can write a fourth power polynomial
polynomial = (2*x + 3)**4
#it outputs in the same format that we entered it.
polynomial

#we can expand the polynomial to see the coefficients of each power:
poly_ex = polynomial.expand()
poly_ex

#The reverse operational is also possible
poly_fct = poly_ex.factor()
poly_fct

#you can use multiple variables, and find specify coefficients
y = symbols('y')
poly_xy = ((y-3)*((x+2)**2)).expand()
print(poly_xy)
print(poly_xy.coeff(x))
print(poly_xy.coeff(y))
print(poly_xy.coeff(x*y))

####Equalities
#Sympy will recognize two expressions which are written in exactly the same way
#This is setting up and equation which sets to two equal to each other.
#the first term is the "left-hand-side" and the second term if the "right-hand-side"
Eq(polynomial,poly_fct)

#Sympy will not immediately recognze two expression written in different ways
Eq(poly_ex,poly_fct)
#however you can ask it to check
Eq(poly_ex,poly_fct).simplify()

#The same behavior will govern the == symbol
polynomoial == poly_fct
poly_ex == polt_fct
#It's okay to use sympy expressions in inequalities, so long as your script has a way to handle false negatives.
#True means "inviable fact of the universe"
#False means "not been shown to be true"

####Differntiation and Integration
#derivative with respect to x
poly_fct.diff(x)

#integral with respect to x
integrate(poly_fct,x)
#note that integrate doesn't produce factors of integration (although dsolve does)

#can it factor that?
integrate(poly_fct,x).factor
#since we only used integers in specifying the coefficients, it thinks we don't want messy factors
#compare what happens if we use floats in the equation
integrate((2.0*x + 3)**4,x).factor
#factor is fairly limited though,
#if we want a precise analytical answer, use roots
roots(integrate(poly_fct,x))

####Solving an Equation
#we can also ask sympy to solve an equation for us.
polynomial = (2*x + 3)**4
poly_y = (2*y + 3)**4
eq=Eq(polynomial,poly_y)
#solve takes an equation as the first arguemnet and the variable to solve for as the second
sol = solve(eq,x)
sol

#the output gives us more than one solution, because it is a fourth order polynomial
#the first solution is the one that we expect, x=y
print(sol[0])
#the second solution looks strange, is it really true?
print(2*sol[1]+3)
print((2*sol[1]+3)**4)
print((2*sol[1]+3)**4-poly_y)

#here capital I is the imaginary number i.
print(I**2)

####Plotting an Equation
#substitute another variable into an expression
print(polynomial)
print(polynomial.subs(x,y-1))

#substitute a specific value into an expression
print(polynomial.subs(x,-1))
print(polynomial.subs(x,0))
print(polynomial.subs(x,1))
print(polynomial.subs(x,2))

#if you are going to make many function evaluations for plotting,
#it's numerically faster to use lambdify
fx = lambdify(x, polynomial)
#fx is a normal function, no longer in the realm of sympy
print(type(polynomial))
print(type(fx))
#make a 1D plot
xvals = np.arange(-2,2,0.1)
plt.plot(xvals,fx(xvals))
plt.show()

#Lambdify can also be used with multiple variables
fxy = lambdify((x,y), (polynomial*poly_y)**(1/4))
yvals = np.arange(-2,2,0.1)
#create a meshgrid
X, Y = np.meshgrid(xvals, yvals, shading='auto')
#make a 2D plot
plt.pcolormesh(X,Y,fxy(X,Y))
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()
plt.show()
