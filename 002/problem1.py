# Question:
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even - valued terms.
# link: https://projecteuler.net/problem=2

totalSum = 0

fibonacci_1 = 1
fibonacci_2 = 2
while(fibonacci_2 <= 4000000):
    if(fibonacci_2 % 2 == 0): 
        totalSum += fibonacci_2
    temp = fibonacci_1 + fibonacci_2
    fibonacci_1 = fibonacci_2
    fibonacci_2 = temp
    
f = open("output.txt","w")
f.write(totalSum.__str__())
# End of Program

# Console output
print(totalSum)
