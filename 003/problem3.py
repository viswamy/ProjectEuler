#
# @Author:Virupaksha Swamy
#
# Question:
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# link: https://projecteuler.net/problem=3

highestPrimeFactor = int(2)
number = int(600851475143) 

while(number > 1):
    if(number % highestPrimeFactor == 0):
        number = int(number/highestPrimeFactor)
    else: 
        highestPrimeFactor = int(highestPrimeFactor + 1)
    
f = open("output.txt","w")
f.write(str(highestPrimeFactor))
# End of Program

# Console output
print(highestPrimeFactor)
