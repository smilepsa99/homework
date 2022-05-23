import math

n = int(input("Enter the number of people : "))

a = math.factorial(365)
b = 365**n
c = math.factorial(365-n)
answer = float(1-a/b*c)

print(answer)