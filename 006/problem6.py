#
# @Author:Virupaksha Swamy
#
# Question:
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n = 100
sum_of_squares = n * (n+1) * (2*n+1) / 6
sum_of_n = n * (n+1) / 2
square_of_sum = sum_of_n * sum_of_n

finalans = square_of_sum - sum_of_squares
f = open("output.txt","w")
f.write(str(finalans))
# End of Program

print(finalans)
