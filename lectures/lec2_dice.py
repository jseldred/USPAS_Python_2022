#example of a script that generates random integer numbers, like rolling dice for a tabletop game.

import numpy as np

#input parameters
#number of dice to be rolled
Ndice = 3
#number of sides of the dice, i.e. random number 1 through Nsides
Nsides = 6
#number to be added to end result
bonus = 2

#make sure all inputs are integer
Ndice = int(Ndice)
Nsides = int(Nsides)
bonus = int(bonus)
#if bonus is negative, set it instead to zero.
bonus = np.max(bonus,0)

#check to see if the Nsides corresponds to one of the regular dice shapes
#if Nsides is equal to one of the listed dice shapes, the sum will be exactly 1
if np.sum(Nsides == np.array([2,4,6,8,12,20])) != 1:
  print(str(Nsides) + " sides, huh? Let me ask the DM...")
  print("Yeah, I guess that's okay.")

#output what is being rolled
print('Rolling ' + str(Ndice) + 'd' + str(Nsides) + '+' + str(bonus) + "...")

#if you give randint a third argument, it will generate an array with each element independently generated.
res_array = np.random.randint(1,Nsides,Ndice)
print('You rolled ' + str(res_array))

#Use sum to find the total, and add the bonus
res = np.sum(res_array)+bonus
print('Result: '+str(res) + '!')

#check to see if the maximum result was obtained.
if res == Nsides*Ndice+bonus:
    print('Woah! You rolled a critical!')
