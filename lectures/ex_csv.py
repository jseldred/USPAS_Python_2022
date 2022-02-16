import numpy as np
import matplotlib.pyplot as plt
import csv

#file intensity data
flist = ['ex_csv_file1.csv', 'ex_csv_file2.csv', 'ex_csv_file3.csv']
fnum = len(flist)

#windowing parameters
tmax = 19500
strp = 39
xstrp = (strp-1)/2
xvals = np.arange(strp)-xstrp

#Data for each file
H_data = np.zeros((tmax,strp,fnum))*np.nan
V_data = np.zeros((tmax,strp,fnum))*np.nan

#Beam Center (mean) and width (sigma)
H_bar = np.zeros(tmax)*np.nan
V_bar = np.zeros(tmax)*np.nan
H_sig = np.zeros(tmax)*np.nan
V_sig = np.zeros(tmax)*np.nan

#load all each csv files
for lp3 in range(fnum):
  filename = flist[lp3]
  #open csv file
  with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #load the entire file into a 2D array at once.
    csv_data = np.array(list(csv_reader)).astype(float)
    #Vertical first, horizontal next
    V_data[:,:,lp3] = csv_data[0:tmax,0:strp]
    H_data[:,:,lp3] = csv_data[0:tmax,strp:(2*strp)]

#Average the data across the three files
H_data2 = np.mean(H_data[:,:,:],2)
V_data2 = np.mean(V_data[:,:,:],2)

for lp in range(tmax):
  #calculate mean
  H_bar[lp] = np.dot(xvals,H_data2[lp,:])/np.sum(H_data2[lp,:])
  V_bar[lp] = np.dot(xvals,V_data2[lp,:])/np.sum(V_data2[lp,:])
  #I could also use numpy.average(xvals, weights=H_data2[lp,:])
  #calculate rms
  H_sig[lp] = np.sqrt(np.dot((xvals-H_bar[lp])**2,H_data2[lp,:])/np.sum(H_data2[lp,:]))
  V_sig[lp] = np.sqrt(np.dot((xvals-V_bar[lp])**2,V_data2[lp,:])/np.sum(V_data2[lp,:]))

#Smooth the data with a moving average
#size of averaging window (in each direction)
awin = 70
#beginning of data to be averaged (early data is unreliable)
tmin = 17
#new arrays for zeros
H_siga = np.zeros(tmax)*np.nan
V_siga = np.zeros(tmax)*np.nan
H_bara = np.zeros(tmax)*np.nan
V_bara = np.zeros(tmax)*np.nan
#Calculate moving average
for lp in range(tmin,tmax):
  #find lower and upper range of the window
  #don't exceed bounds of the data
  tlo = np.max((tmin,lp-awin))
  thi = np.min((tmax,lp+awin))
  H_bara[lp] = 1.5*np.nanmean(H_bar[tlo:thi])
  V_bara[lp] = 1.5*np.nanmean(V_bar[tlo:thi])
  H_siga[lp] = 1.5*np.nanmean(H_sig[tlo:thi])
  V_siga[lp] = 1.5*np.nanmean(V_sig[tlo:thi])

#Plot beam sigmas
plt.plot(H_siga,label='Horz')
plt.plot(V_siga,label='Vert')
plt.xlabel('Revolutions')
plt.ylabel('Beam RMS (mm)')
plt.title('Beam RMS over Time')
plt.legend()
plt.savefig('ex_csv_1.png', bbox_inches='tight')
plt.show()
#Yes, the horizontal data is very noisy!

#Plot beam orbit
plt.plot(H_bara,label='Horz')
plt.plot(V_bara,label='Vert')
plt.xlabel('Revolutions')
plt.ylabel('Beam orbit (mm)')
plt.title('Beam Orbit over Time')
plt.legend()
plt.savefig('ex_csv_1.png', bbox_inches='tight')
plt.show()
