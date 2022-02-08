from math import factorial

num = factorial(100)

sumOfDigits = sum([int(x) for x in str(num)])
print(sumOfDigits)