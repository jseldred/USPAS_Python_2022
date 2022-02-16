#example of updating a plot in real-time and example of creating an animation.

import numpy as np
import matplotlib.pyplot as plt
#needed to tell the code to wait
import time
#neded to save an animation
import matplotlib.animation as animation 

####Real-time Animation/Updating

#setup parabola
a = np.arange(-1,1,0.1)
x = np.arange(-3,3,0.01)
y = -a[0]*x**2

#This creates a figure and axes object
fig, ax = plt.subplots()
#even though nothing has been plotted yet, set the limits for the animation
plt.xlim([-3,3])
plt.ylim([-3,3])
#creates a line object, like what is created when you call plt.plot(x,y)
#take note of the comma
line_obj, = ax.plot([], [], linewidth=2)

#Update plot every 0.1*s
for lp in range(len(a)):
  y = -a[lp]*x**2
  line_obj.set_data(x,y)
  #draw, not show, means that it is allowed to change.
  plt.draw()
  #the plot doesn't actually update until you pause, no matter how briefly
  plt.pause(0.001)
  #wait 0.1~seconds
  time.sleep(0.1)

#Now let's animate in reverse
for lp in range(len(a)):
  y = -a[len(a)-lp-1]*x**2
  line_obj.set_data(x,y)
  #draw, not show, means that it is allowed to change.
  plt.draw()
  #the plot doesn't actually update until you pause, no matter how briefly
  plt.pause(0.001)
  #wait 0.1~seconds
  time.sleep(0.1)

#this prevents the script from continuing until you lose the window
plt.show()

####To save an animation to file
#animation progression function 
def animate(lp): 
  #lp here is the lpth frame
  if lp < len(a):
    y = -a[lp]*x**2
  else:
    y = -a[2*len(a)-lp-1]*x**2
  line_obj.set_data(x, y) 
  return line_obj,

frames_per_sec = 15
ms_per_frame = 1000/frames_per_sec

fig, ax = plt.subplots()
plt.xlim([-3,3])
plt.ylim([-3,3])
line_obj, = ax.plot([], [], linewidth=2)

#create an animation object
anim = animation.FuncAnimation(fig, animate, frames = 2*len(a), interval = ms_per_frame, blit = True)

#save that object as a gif
anim.save('ex_anim_parabola.gif', writer = 'ffmpeg', fps = frames_per_sec)
#anim.save('ex_anim_parabola.mp4', writer = 'ffmpeg', fps = frames_per_sec)
