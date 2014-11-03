#
# @Author:Virupaksha Swamy
#
# Question:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(a, b):
    if(a == b):
        return a
    if(a > b):
        if(a % b == 0):
            return b
        return gcd(a % b, b)
    elif(a < b):
        if(b % a == 0):
            return a
        return gcd(a, b% a)
    

def lcm(a, b):
    return a * b / gcd(a,b)

finalans = 1
for i in range(2,21):
    finalans = lcm(finalans,i)
     
f = open("output.txt","w")
f.write(str(finalans))
# End of Program

print(finalans)
