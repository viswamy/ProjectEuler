#
# @Author:Virupaksha Swamy
#
# Question:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers.

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
