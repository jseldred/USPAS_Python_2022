#example of a script that calculate various statistical properties of a Gaussian sample

import numpy as np
import matplotlib.pyplot as plt

#create a sample of 20 numbers with a random normal distribution
snum = 20
x = np.random.normal(0,1,snum)

print('The maximum value in this sample is ' + str(np.max(x)))
print('The minimum value in this sample is ' + str(np.min(x)))
print('The average value of this sample is ' + str(np.mean(x)))
print('The standard deviation of this sample is ' + str(np.std(x)))
print('The median value of this sample is '  + str(np.median(x)))
print('The 75% percentile of this sample is ' + str(np.quantile(x,0.75)))
print('The 25% percentile of this sample is ' + str(np.quantile(x,0.25)))

#That's interesting but how do these quantities vary with sample size?

snum2 = 2000
x = np.random.normal(0,1,snum2)

smax = np.zeros(snum2-snum)
smin = np.zeros(snum2-snum)
smean = np.zeros(snum2-snum)
sdev = np.zeros(snum2-snum)
smed = np.zeros(snum2-snum)
s75p = np.zeros(snum2-snum)
s25p = np.zeros(snum2-snum)
for lp in np.arange(snum2-snum):
  dex = lp+snum
  smax[lp] = np.max(x[:dex])
  smin[lp] = np.min(x[:dex])
  smean[lp] = np.mean(x[:dex])
  sdev[lp] = np.std(x[:dex])
  smed[lp] = np.median(x[:dex])
  s75p[lp] = np.quantile(x[:dex],0.75)
  s25p[lp] = np.quantile(x[:dex],0.25)

s = np.arange(snum,snum2)

#Demonstrates use of a legend
plt.plot(s,smax,label='max')
plt.plot(s,smin,label='min')
plt.plot(s,smean,label='mean')
plt.plot(s,sdev,label='stdev')
plt.plot(s,smed,label='median')
plt.plot(s,s75p,label='75%')
plt.plot(s,s25p,label='25%')
plt.legend(loc="upper right")
plt.xlabel('Numbers in Sample')
plt.title('Numerics of Normal Distribution')
plt.savefig('lec2_stat_1.png', bbox_inches='tight')
plt.show()

#Demonstate use of a log x-scale
plt.semilogx(s,smax,label='max')
plt.semilogx(s,smin,label='min')
plt.semilogx(s,smean,label='mean')
plt.semilogx(s,sdev,label='stdev')
plt.semilogx(s,smed,label='median')
plt.semilogx(s,s75p,label='75%')
plt.semilogx(s,s25p,label='25%')
plt.legend(loc="upper right")
plt.xlabel('Numbers in Sample (log)')
plt.title('Numerics of Normal Distribution')
plt.savefig('lec2_stat_2.png', bbox_inches='tight')
plt.show()
