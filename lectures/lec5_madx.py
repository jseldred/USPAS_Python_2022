#Example of i/o, and using Python to run another program
#We will run MADX, read the output file, change the lattice file, run MADX again, read the output again, and compare the results.
#Not sure if this will work on your computer or not.
import os
import sys
from tkinter import E

####Run the MADX file

#We need to run the MADX file to ensure the output is up to date.
#we use os.chdir to change directory into the MADX folder
try:
  os.chdir("MADX")
  #Python directs the terminal to run MADX
  os.system('madx BoosterSF.madx')
  os.chdir("..")
  #if we were to use os.system(cd), it wouldn't work like we want it to
except:
  #if the try statements fail, this statement runs instead
  sys.exit('Error running MADX. Check files and directory')

####Read the Output file
#This opens a file for reading
try:
  file_lat = open('MADX/BoosterSF_out.tfs ', 'r')
except:
  sys.exit('Error opening TFS file. Check files and directory')
#This reads in the lines of the file as a list of strings
Lines_out = file_lat.readlines()

#Here are some lines we can see
print(Lines_out[0])
print(Lines_out[1])
print(Lines_out[2])
print(Lines_out[3])
print(Lines_out[4])
print(Lines_out[5])

#Lets search for the tunes and store them
#find looks for a string inside another string
#find is -1 if it doesn't find it and the index where the string starts if it does
#split turns a string into a list separated by the split string
for line in Lines_out:
  if (line.find('Q1') != -1 and line.find('DQ') == -1):
    print(line.split('%le'))
    Q1i = float(line.split('%le')[1])
  elif (line.find('Q2') != -1 and line.find('DQ') == -1):
    print(line.split('%le'))
    Q2i = float(line.split('%le')[1])

print(Q1i)
print(Q2i)
file_lat.close()


####Read and Change the LAT file
#Read in the MADX Lattice file
try:
  file_lat = open('MADX/BoosterSF.lat', 'r')
except:
  sys.exit('Error opening LAT file. Check files and directory;')
Lines_lat = file_lat.readlines()

#Find a specific expression qfk1 in a line, find its value, and change it.
#the value of qfk1 is between '=' and ';', so split it into three strings based on that.
#cast the middle string as a float, change it, cast it back as a string
#finall we concatenate the three strings and replace original line.
for lp in range(len(Lines_lat)):
  line = Lines_lat[lp]
  if (line.find('qfk1') != -1 and line.find('qfk1') < 4):
    print(line)
    print(line.split('='))
    str1 = line.split('=')[0] + str('=')
    str2 = line.split('=')[1]
    print(str2.split(';'))
    str3 = str(';') + str2.split(';')[1]
    qfk1 = float(str2.split(';')[0])
    print(qfk1)
    qfk1=qfk1*1.05
    str2 = str(qfk1)
    qf_out = str1 + str2 + str3
    print(qf_out)
    Lines_lat[lp] = qf_out

file_lat.close()

#Use the read-in lines and changed line to rewrite the file
#since the last statement was successful, I don't need to try/except this one
file_lat = open('MADX/BoosterSF.lat', 'w')
file_lat.writelines(Lines_lat)
file_lat.close()


####Run the MADX file again

#Now that we have changed the value of the .lat file, we want to run the .madx file
#since the last statement was successful, I don't need to try/except this one
os.chdir("MADX")
os.system('madx BoosterSF.madx')
os.chdir("..")


####Read the Output file again

#running that MADX file should have generated/updated the .tfs file so now we can read that
#since the last statement was successful, I don't need to try/except this one
file_lat = open('MADX/BoosterSF_out.tfs ', 'r')
sys.exit('Error opening TFS file. Check files and directory')
Lines_out = file_lat.readlines()

#what effect did changes the quad have on the tune?
for line in Lines_out:
  if (line.find('Q1') != -1 and line.find('DQ') == -1):
    print(line.split('%le'))
    Q1f = float(line.split('%le')[1])
  elif (line.find('Q2') != -1 and line.find('DQ') == -1):
    print(line.split('%le'))
    Q2f = float(line.split('%le')[1])

print('Q1 changed from ' + str(Q1i) + ' to ' + str(Q1f))
print('Q2 changed from ' + str(Q2i) + ' to ' + str(Q2f))
file_lat.close()
