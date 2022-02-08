'''
Name: Sebastian Vega
Description:
    find the largest prime factor of a given number

    can only really use prime factorization
'''

from math import sqrt

def isPrime(num):
    '''
    num: number to check -> integer
    :return: if the number is a prime number
    :rtype: boolean
    '''
    isPrime = True # initially set to True

    for factor in range(2, round(sqrt(num))+1): # range of two to the approximate square root of the number, anything after that would be duplicate factor pairs and therefore redundant
        if num % factor == 0: # if divisible 
            isPrime = False # set prime to False

    return isPrime

def isFactor(current, num):
    '''
    current: number to check -> integer
    num: number to check against -> integer
    :return: if current is a factor of num
    :rtype: boolean
    '''
    prime = isPrime(current) # check if current number is prime
    if prime and num % current == 0: # if divisible
        return True

    return False

def primeFactorization(current, num):
    '''
    current: current number we are on -> integer
    num: original number -> integer
    description:
        essentially a prime factorization loop with an exit condition of two last
        "factors" being prime meaning the prime factorization would be complete
    '''
    while True:
        if isFactor(current, num): # checks if the current term is a prime factor of the current number
            num = num // current # divide the current number by the current factor to reset the prime factorization process for the next iteration
            primes.append(current) # add current factor to primes list
        else:
            current += 1 # go to next number

        if isFactor(current, current) and isFactor(num, num): # essentially if all factors are prime, we have completed the prime factorization
            primes.append(num) # add the transformed num to the primes as it is now also a prime factor of the original num
            break # exit the loop

if __name__ == "__main__":
    num = 600851475143 # number in project euler problem description
    primes = [] # keeps list of all prime factors of num
    current = 2 # start at 2 as it is the lowest prime number
    
    primeFactorization(current, num) # calls prime factorization loop
    
    print(max(primes)) # prints largest prime factor of original number
