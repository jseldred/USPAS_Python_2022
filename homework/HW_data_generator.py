import numpy as np
import matplotlib.pyplot as plt
import csv

tnum = 1000

f_c = 1/7.0
f_m = 1/17.0
a_m = 1.0
aerr = 5*10.0**(-1)
feer = 5*10.0**(-1)

x = np.zeros(tnum)

for lp in range(tnum):
  x[lp] = np.cos( 2*np.pi*f_c*lp + a_m*np.sin(2*np.pi*f_c*lp) +feer*np.random.normal()) +aerr*np.random.normal()

with open('HW_data', mode='w') as csv_file:
  csv_write = csv.writer(csv_file, delimiter=' ')
  csv_write.writerow(x.tolist())
