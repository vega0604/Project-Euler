'''
Name: Sebastian Vega
Description:
    A palindromic number reads the same both ways. The largest palindrome made from the product of 
    two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
'''
palindromes = [] # keeps list of all palindromes from 100 - 1000(all three digit numbers)

for x in range(100, 1000): # first 3 digit number loop
    for y in range(100, 1000): # second 3 digit number loop
        if str(x*y) == str(x*y)[::-1]: # checks if product of both 3 digit numbers is the same forwards as it is backwards(palindromic)
            palindromes.append(x*y) # adds palindrome to palindromes list

print(max(palindromes)) # prints largest palindrome