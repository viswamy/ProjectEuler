# This program finds the sum of numbers below 1000 which are divisible by either 3 or 5

totalSum = 0
for i in range(1, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        totalSum += i
  
f = open("output.txt","w")
f.write(totalSum.__str__())

#End of Program

#Console output
print(totalSum)