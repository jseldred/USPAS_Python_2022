#Matching script to be used in homework exercise
#import packages
import numpy as np
import sys
import csv

#output this error if the script is called incorrectly.
if len(sys.argv) != 5:
  print("incorrect number of arguments")
  sys.exit()

#Four input arguments in this sequence
betax_in = float(sys.argv[1])
alphax_in = float(sys.argv[2])
betay_in = float(sys.argv[3])
alphay_in = float(sys.argv[4])

#Horizontal transfer matrix and beta matrix
Mx = np.matrix([[-2.5136, 4.128], [-0.72256, 0.7888]])
Mbx = np.matrix([ [Mx[0,0]**2,-2*Mx[0,0]*Mx[0,1],Mx[0,1]**2],[-Mx[0,0]*Mx[1,0],Mx[0,0]*Mx[1,1]+Mx[0,1]*Mx[1,0],-Mx[0,1]*Mx[1,1]],[Mx[1,0]**2,-2*Mx[1,0]*Mx[1,1],Mx[1,1]**2] ])

#Obtain outgoing horizontal TWISS parameters
gammax_in = (1+alphax_in**2)/betax_in
xin = np.array([betax_in,alphax_in,gammax_in]).T
xout = np.array(np.dot(Mbx,xin))[0]
betax_out = xout[0]
alphax_out = xout[1]

#Vertical transfer matrix and beta matrix
My = np.matrix([[0.3664, 0.672], [-1.58144, -0.1712]])
Mby = np.matrix([ [My[0,0]**2,-2*My[0,0]*My[0,1],My[0,1]**2],[-My[0,0]*My[1,0],My[0,0]*My[1,1]+My[0,1]*My[1,0],-My[0,1]*My[1,1]],[My[1,0]**2,-2*My[1,0]*My[1,1],My[1,1]**2] ])

#Obtain outgoing vertical TWISS parameters
gammay_in = (1+alphay_in**2)/betay_in
yin = np.array([betay_in,alphay_in,gammay_in]).T
yout = np.array(np.dot(Mby,yin))[0]
betay_out = yout[0]
alphay_out = yout[1]

#Output outgoing TWISS parameters to betas_out file
with open('betas_out', mode='w') as csv_file:
  csv_write = csv.writer(csv_file, delimiter=' ')
  csv_write.writerow([betax_out,alphax_out,betay_out,alphay_out])
