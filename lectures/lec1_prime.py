#example of a script that finds and prints all the prime numbers between 1 and 100

#loop through all numbers 1 to 100 (starts at 1 ends at 100)
for lp in range(1,101):
    #create a variable that keeps track of whether lp is prime
    #assume lp is prime until proven otherwise
    prime_flag = 1
    #check whether lp is prime by checking if it is divisible by any number 2 to lp-1
    #use a 'while' loop, rather than a 'for' loop, so that we can stop checking if we find lp is not prime. 
    lp2 = 2
    while (lp2 < lp and prime_flag == 1):
        #is lp evenly divisible by lp2?
        #int truncates the remainder, so we can use that to check for a remainder
        if (lp/lp2 == int(lp/lp2)):
            prime_flag = 0
        
        #at the end of the 'while' loop, iterate lp2 because it doesn't happen automatically.
        lp2 = lp2 + 1
    
    #print if lp is prime (after checking all the numbers)
    if (prime_flag == 1):
        print(lp)

#end of program
