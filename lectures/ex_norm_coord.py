#example of a script that creates a 4D gaussian distribution, then transforms it to physical coordinates,
#then propagates it, then transforms back to normalized coordinates

import numpy as np
import matplotlib.pyplot as plt

####transform normalized into physical coordinates
#this function will work if you don't give it orbit coordinates, but you must give it TWISS values
def NormToPhys(fnorm_coords,fbetax,falphax,fbetay,falphay,fx0=0.0,fxp0=0.0,fy0=0.0,fyp0=0.0):
  #expects 4 by np.size(x,1) array
  fphys_coords = fnorm_coords*np.nan
  #x = sqrt(betax)*Xn
  fphys_coords[0,:] = fnorm_coords[0,:]*np.sqrt(fbetax)+fx0
  #xp = -alphax*Xn/sqrt(betax) + PXn/sqrt(betax)
  fphys_coords[1,:] = (-falphax*fnorm_coords[0,:] + fnorm_coords[1,:]) / np.sqrt(fbetax) + fxp0
  fphys_coords[2,:] = fnorm_coords[2,:]*np.sqrt(fbetay)+fy0
  fphys_coords[3,:] = (-falphay*fnorm_coords[2,:] + fnorm_coords[3,:]) / np.sqrt(fbetay) + fyp0
  return fphys_coords

####transform physical into normalized coordinates
#this function will work if you don't give it orbit coordinates, but you must give it TWISS values
def PhysToNorm(fphys_coords,fbetax,falphax,fbetay,falphay,fx0=0.0,fxp0=0.0,fy0=0.0,fyp0=0.0):
  #expects 4 by np.size(x,1) array
  fnorm_coords = fphys_coords*np.nan
  #Xn = x/sqrt(betax)
  fnorm_coords[0,:] = (fphys_coords[0,:]-fx0)/np.sqrt(fbetax)
  #PXn = alphax*x/sqrt(betax) + xp*sqrt(betax)
  fnorm_coords[1,:] = falphax*(fphys_coords[0,:]-fx0)/np.sqrt(fbetax) + (fphys_coords[1,:]-fxp0)*np.sqrt(fbetax)
  fnorm_coords[2,:] = (fphys_coords[2,:]-fy0)/np.sqrt(fbetay)
  fnorm_coords[3,:] = falphay*(fphys_coords[2,:]-fy0)/np.sqrt(fbetay) + (fphys_coords[3,:]-fyp0)*np.sqrt(fbetay)


####generate an initial random distribution
#its easier to generate a random distribution in normalized coordinates,
#because the sigma is the same in each direction and there is no tilt from alpha.

#number of particles
pnum = 10000

#generate Gaussian distribution
mean_list = [0.0,0.0,0.0,0.0]
#geometric rms emittance, not to be confused with normalized emittance (which refers to a different type of normalization)
#If the units of emittance are micrometer or mm-mrad, then the units of the physical coordinates will be mm, mrad
#Sometimes you will see "pi" in the units of emittance, and I'm ignoring it because it comes out anyway.
eps_x = 1.0 #mm mrad
eps_y = 1.0 #mm mrad
sig_list = [np.sqrt(eps_x),np.sqrt(eps_x),np.sqrt(eps_y),np.sqrt(eps_y)]
norm_coords = np.random.normal(mean_list[0], sig_list[0], pnum)
for lp in range(1,4):
  norm_coords = np.vstack((norm_coords,np.random.normal(mean_list[lp], sig_list[lp], pnum)))

#norm_coords is a 2D array with 4 by pnum
#Here norm_coords stands for all four normalized coordinates typically Xn, PXn, Yn, PYn for each particle
print(np.size(norm_coords,0))
print(np.size(norm_coords,1))

#This is where you would truncate the outliers, if you want to.


####Initial Physical Coordinates
#you need to propagate particles in physical coordinates


#The starting TWISS values are whatever will give you an accurate description of the shape your ellipse in physical coordinates
#You might try to match your beamline to your starting distribution or you might try to match youe starting distribution to your beamline.
#Or you may take it as it is as just understand what the output distribution looks like.
use_match = 0
if (use_match == 1):
  #These TWISS and orbit values are what will generate a matched distribution in the transfer matrix I'm going to use
  betax0=8.15183121
  alphax0=-3.26089667
  betay0=0.67522372
  alphay0=0.27009059
  #start with beam centered on beamline
  x0 = 0.0
  xp0 = 0.0
  y0 = 0.0
  yp0 = 0.0
else:
  #I am picking some most random values
  #that means the initial and final distribution will look different
  betax0=10.0
  alphax0= -5.0
  betay0=1.0
  alphay0=0.0
  #start with slight displacements
  x0 = 1.0
  xp0 = -0.5
  y0 = 0.2
  yp0 = 0.1

#obtain the physical coordinates
phys_coords0 = NormToPhys(norm_coords,betax0,alphax0,betay0,alphay0,x0,xp0,y0,yp0)

#what do the initial physical coordinates look like in x-xp?
plt.scatter(phys_coords0[0,:],phys_coords0[1,:],s=2)
plt.xlabel('physical coordinate x (mm)')
plt.ylabel('physical coordinate x-prime (mrad)')
#used to set the same scale in both coordinates
qmin = np.min((np.min(phys_coords0[0,:]),np.min(phys_coords0[1,:])))
qmax = np.max((np.max(phys_coords0[0,:]),np.max(phys_coords0[1,:])))
plt.xlim((1.1*qmin,1.1*qmax))
plt.ylim((1.1*qmin,1.1*qmax))
plt.show()

#what do the initial physical coordinates look like in x-y?
plt.scatter(phys_coords0[0,:],phys_coords0[2,:],s=2)
plt.xlabel('physical coordinate x (mm)')
plt.ylabel('physical coordinate y (mm)')
#used to set the same scale in both coordinates
qmin = np.min((np.min(phys_coords0[0,:]),np.min(phys_coords0[2,:])))
qmax = np.max((np.max(phys_coords0[0,:]),np.max(phys_coords0[2,:])))
plt.xlim((1.1*qmin,1.1*qmax))
plt.ylim((1.1*qmin,1.1*qmax))
plt.show()

#for simplicity, I am doing a scatterplot, but to see the density of particles you should do a hist2d


####Propagate Coordinates through Lattice
#you need to propagate particles in physical coordinates

#transfer matrices
#if you don't have a transfer matrix you need to calculate one specific to your line.
#these are taken from my beta_match example, which correspond to 3/4 of the way through a quad in a FODO cell, all as one block
#for your projects, you probably want to multiple one matrix at a time, using whatever variables you are varying
Mx = np.matrix([[-2.5136, 4.128], [-0.72256, 0.7888]])
My = np.matrix([[0.3664, 0.672], [-1.58144, -0.1712]])

#The physical coordinates are now changed as a result of a single-pass through Mx and My
#If this were a ring, it would represent a single revolution, and I could keep track of behavior for many turns
phys_coords1 = np.zeros((4,pnum))*np.nan
phys_coords1[0:2,:] = Mx*np.matrix(phys_coords0[0:2,:])
phys_coords1[2:4,:] = My*np.matrix(phys_coords0[2:4,:])

#what do the final physical coordinates look like in x-xp?
plt.scatter(phys_coords0[0,:],phys_coords0[1,:],s=2,label='initial')
plt.scatter(phys_coords1[0,:],phys_coords1[1,:],s=2,label='final')
plt.xlabel('physical coordinate x (mm)')
plt.ylabel('physical coordinate x-prime (mrad)')
#used to set the same scale in both coordinates
qmin = np.min(( np.min((np.min(phys_coords1[0,:]),np.min(phys_coords1[1,:]))) , np.min((np.min(phys_coords0[0,:]),np.min(phys_coords0[1,:]))) ))
qmax = np.max(( np.max((np.max(phys_coords1[0,:]),np.max(phys_coords1[1,:]))) , np.max((np.max(phys_coords0[0,:]),np.max(phys_coords0[1,:]))) ))
plt.xlim((1.1*qmin,1.1*qmax))
plt.ylim((1.1*qmin,1.1*qmax))
plt.legend()
plt.savefig('ex_norm_coord_1.png', bbox_inches='tight')
plt.show()

#what do the final physical coordinates look like in x-y?
plt.scatter(phys_coords0[0,:],phys_coords0[2,:],s=2,label='initial')
plt.scatter(phys_coords1[0,:],phys_coords1[2,:],s=2,label='final')
plt.xlabel('physical coordinate x (mm)')
plt.ylabel('physical coordinate y (mm)')
#used to set the same scale in both coordinates
qmin = np.min(( np.min((np.min(phys_coords1[0,:]),np.min(phys_coords1[2,:]))) , np.min((np.min(phys_coords0[0,:]),np.min(phys_coords0[2,:]))) ))
qmax = np.max(( np.max((np.max(phys_coords1[0,:]),np.max(phys_coords1[2,:]))) , np.max((np.max(phys_coords0[0,:]),np.max(phys_coords0[2,:]))) ))
plt.xlim((1.1*qmin,1.1*qmax))
plt.ylim((1.1*qmin,1.1*qmax))
plt.legend()
plt.savefig('ex_norm_coord_2.png', bbox_inches='tight')
plt.show()


####Propagate TWISS and orbit through the lattice
#once you have the physical coordinates at the end of the lattice, you might not need anything else.
#however this is how you can propagate the TWISS variables and orbits

#Define the 3x3 beta matrix
Mbx = np.matrix([ [Mx[0,0]**2,-2*Mx[0,0]*Mx[0,1],Mx[0,1]**2],[-Mx[0,0]*Mx[1,0],Mx[0,0]*Mx[1,1]+Mx[0,1]*Mx[1,0],-Mx[0,1]*Mx[1,1]],[Mx[1,0]**2,-2*Mx[1,0]*Mx[1,1],Mx[1,1]**2] ])
Mby = np.matrix([ [My[0,0]**2,-2*My[0,0]*My[0,1],My[0,1]**2],[-My[0,0]*My[1,0],My[0,0]*My[1,1]+My[0,1]*My[1,0],-My[0,1]*My[1,1]],[My[1,0]**2,-2*My[1,0]*My[1,1],My[1,1]**2] ])

#use the beta matrix to propage TWISS
gammax0 = (1+alphax0**2)/betax0
twissx0 = np.array([betax0,alphax0,gammax0]).T
twissx1 = np.array(np.dot(Mbx,twissx0))[0]
betax1 = twissx1[0]
alphax1 = twissx1[1]

gammay0 = (1+alphay0**2)/betay0
twissy0 = np.array([betay0,alphay0,gammay0]).T
twissy1 = np.array(np.dot(Mby,twissy0))[0]
betay1 = twissy1[0]
alphay1 = twissy1[1]

#use the standard transfer matrix to propagate orbit
orbit0 = np.matrix([x0, xp0, y0, yp0]).T
orbit1 = orbit0*np.nan
orbit1[0:2] = Mx*(orbit0[0:2])
orbit1[2:4] = My*(orbit0[2:4])
x1 = orbit1[0]
xp1 = orbit1[1]
y1 = orbit1[2]
yp1 = orbit1[3]

#If we wanted to convert back to normalized coordinates, we now have what we would need
#one reason to do that would be to measure the emittance-growth

####Final Thoughts on Orbit
#keep in mind this orbit is relative to the Frenet-Serret defined reference orbit
#which means a centered orbit 0,0,0,0 going through a dipole bend will remain 0,0,0,0 coming out of the dipole
#even though the reference orbit is in actuality curved.

#you can do a dipole (aka closed-orbit) corrector/error, which won't be reflected in the reference orbit, by adding a kick in one dimension.
thx = 0.002 #mrad correction
thy = 0.0 #mrad correction
corr = np.array([0,thx,0,thy])
#needed to add the correction to all the particles
corr_2D = np.matrix(corr).T*np.matrix(np.ones(pnum))
phys_coords1 =  phys_coords0 + corr_2D

#you can do a misaligned element by subtracting an offset from the orbit,
#multiplying through the misaligned element, and then reimposing the offset.
mx = 0.1 #mm
my = 0.0 #mm
miss = np.array([mx,0,my,0])
miss_2d = np.matrix(miss).T*np.matrix(np.ones(pnum))
f1 = 3 #focal length
QFx = np.matrix([[1,0],[-1/f1,1]])
QFy = np.matrix([[1,0],[1/f1,1]])
mis_coord = phys_coords0 - miss_2d
mis_coord[0:2,:] = QFx*np.matrix(mis_coord[0:2,:])
mis_coord[2:4,:] = QFy*np.matrix(mis_coord[2:4,:])
phys_coords1 = mis_coord + miss_2d
#in this example, I could have also represented the misaligned quadrupole as a dipole error.
