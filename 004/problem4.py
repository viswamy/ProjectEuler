#
# @Author:Virupaksha Swamy
#
# Question:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers.

finalans = 0

for i in range(1,1000):
        for j in range(1,1000):
                product = i * j
                productstr = str(product)
                productstrrev = productstr[::-1]
                productrev = int(productstrrev)
                if(product == productrev):
                        if(finalans < product):
                                finalans = product

f = open("output.txt","w")
f.write(str(finalans))
# End of Program


print(finalans)
