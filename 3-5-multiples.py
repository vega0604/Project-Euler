'''
Name: Sebastian Vega
Description: 
    calculates the sum of all the multiples of 3 or 5 below 1000

'''

# Uses list comprehension to check if a number is a multiple of 3 or 5
# a number is a multiple of 3 or 5 if the remainder of a division between the number and 3 or 5 is 0
# hence the modulo operator.
divisors = sum([x if x % 3 == 0 or x % 5 == 0 else 0 for x in  range(1000)])
print(divisors)