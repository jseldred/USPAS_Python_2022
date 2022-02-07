#example of a script the converts angles in radians to degrees and back

#imports numpy package, and now we refer to it as np
import numpy as np

#defines a function which take deg as an argument
def deg2rad(deg):
    temp = deg/180.0
    #use numpy's numerical estimate of pi
    temp = temp*np.pi
    #use numpy's rounding method
    #round to the nearest three decimal places
    temp = np.round(temp,3)
    return temp

#defines a function, takes rad as an argument
def rad2deg(rad):
    #I can do it all on one line if I want
    #round to the nearest tenth degree
    return np.round(rad*180.0/np.pi,1) 

#Now the main program actually starts

#define a sequence of angles in radian
ang_list = np.array([0, 0.25, 0.5, 0.75])*np.pi
ang_list = np.round(ang_list,3)
ang_list_num = len(ang_list)

#loop through the list of angles
for lp in range(ang_list_num):
    #ang_rad is the element in the list corresponding to lp
    ang_rad = ang_list[lp]
    #ang_deg is found by converting ang_rad
    ang_deg = rad2deg(ang_rad)
    print ("Converting " + str(ang_rad) + " radians into " + str(ang_deg) + " degrees.")

#here is another way to do it, use the angle as the loop variable
#specify how much the angle will increase each loop
ang_deg = 0
ang_itr = 30
ang_max = 100

#loop until max is exceeded
while (ang_deg < ang_max):
    #we already have the first value of ang_deg
    #ang_rad is found by converting ang_deg
    ang_rad = deg2rad(ang_deg)
    print ("Converting " + str(ang_deg) + " degrees into " + str(ang_rad) + " radians.")
    #increase the value of ang_deg for the next loop
    ang_deg = ang_deg + ang_itr

