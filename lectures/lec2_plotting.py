#Several basic examples of 1D plots

import numpy as np
import matplotlib.pyplot as plt

####Simple Plots
#define some 1D arrays
x = np.arange(-20,21)
quad = x**2
cub = x**3

#Basic plot
#plot x, y
plt.plot(x,quad)
plt.show()

#if you don't specify x, it will defaults to range(0,len(y))
plt.plot(quad)
plt.show()

#if you plot multiple lines, it will automatically assign them unique colors
plt.plot(x,quad)
plt.plot(x,cub)
plt.show()

####Customizing Plots
#but you can choose the colors, either by name or rgb values
plt.plot(x,quad,color='red')
#red 0 to 1, green 0 to 1, blue to 1 -> this should be green
plt.plot(x,cub,color=(0.1, 0.5, 0.2))
plt.show()

#how to give your plot axis labels and a title
plt.plot(x,quad)
plt.plot(x,cub)
plt.xlabel('Linearly increasing variable x')
plt.ylabel('Power of x')
plt.title('Quadratic vs Cubic powers')
plt.show()

#cubic is somewhat out of scale, you can redefine the axis limits with
plt.plot(x,quad)
plt.plot(x,cub)
plt.xlabel('Linearly increasing variable x')
plt.ylabel('Power of x')
plt.title('Quadratic vs Cubic powers')
plt.ylim(-1000,1000)
plt.show()

#label your plot with a legend
plt.plot(x,quad,label='quadratic')
plt.plot(x,cub,label='cubic')
plt.xlabel('Linearly increasing variable x')
plt.ylabel('Power of x')
plt.title('Quadratic vs Cubic powers')
plt.ylim(-1000,1000)
plt.legend()
plt.show()

#when you are publishing a plot, you often want the font bigger than this
sz1 = 10
sz2 = 12
sz3 = 14
plt.plot(x,quad,label='quadratic',linewidth=3)
plt.plot(x,cub,label='cubic',linewidth=3)
plt.xlabel('Linearly increasing variable x', fontsize=sz2)
plt.ylabel('Power of x', fontsize=sz2)
plt.title('Quadratic vs Cubic powers', fontsize=sz3)
plt.ylim(-1000,1000)
plt.legend()
plt.rc('xtick', labelsize=sz1)    # fontsize of the tick labels
plt.rc('ytick', labelsize=sz1)    # fontsize of the tick labels
plt.rc('legend', fontsize=sz1)    # legend fontsize
#this line saves a png to the current directory
#does not work if you put savefig after show
plt.savefig('lec2_plotting_1.png', bbox_inches='tight')
plt.show()

####Scatterplots
#scatter plots can take a third variable which represents markers size
#scatter plots can also take a fourth variable for color along a colormap
plt.scatter(x,cub,quad,cub)
plt.show()

#specifying a colormap
plt.scatter(x,cub,quad,cub,cmap="magma")
plt.show()

####Using Colormaps Explicitly
#define an array of colormpas vectors
import matplotlib.cm as cm
pnum = 7
c_list = plt.cm.viridis(np.linspace(0, 1, pnum))
print(c_list)

#loop through a plot
x = np.arange(-20,21,0.1)
for lp in range(pnum):
  plt.plot(x,x**lp,color=c_list[lp],linewidth=3,label='power of '+str(lp))

plt.xlabel('Linearly increasing variable x')
plt.title('Powers of x', fontsize=sz3)
plt.ylim(-1000,1000)
plt.legend()
plt.show()
