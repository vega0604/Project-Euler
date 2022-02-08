'''
Name: Sebastian Vega
Description:
    find the smallest natural number divisible by all numbers from 1-20(inclusive)

    essentially the product of the highest exponent prime factors in all the 
    prime factorizations of the numbers from 1-20

    16 = 2 x 2 x 2 x 2 = 2^4
    17 = 17
    18 = 2 x 3 x 3 = 2 x 3^2

    hence 2^4 x 3^2 x 17 = 2448
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

def primeFactorization(num):
    '''
    current: current number we are on -> integer
    num: original number -> integer
    description:
        essentially a prime factorization loop with an exit condition of two last
        "factors" being prime meaning the prime factorization would be complete
    '''

    current = 2

    primes = []
    while True:
        if isFactor(current, num): # checks if the current term is a prime factor of the current number
            num = num // current # divide the current number by the current factor to reset the prime factorization process for the next iteration
            primes.append(current) # add current factor to primes list
        else:
            current += 1 # go to next number

        if isFactor(current, current) and isFactor(num, num): # essentially if all factors are prime, we have completed the prime factorization
            primes.append(num) # add the transformed num to the primes as it is now also a prime factor of the original num
            break # exit the loop

    return primes



if __name__ == '__main__':
    factors = []
    for x in range(2, 21):
        factors.append(primeFactorization(x))

    print(factors)
    exponents = {}
    for arr in factors:
        for factor in arr:
            exponents[factor] = arr.count(factor)
            if arr.count(factor) > exponents[factor]:
                exponents[factor] = arr.count(factor)
                break

    product = 1

    for factor in exponents:
        product *= factor^exponents[factor]

    print(product)

