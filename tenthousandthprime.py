def isPrime(num):
    for n in range(2, round(num**0.5)+1):
        if num % n == 0:
            return False

    return True

primes = []

num = 2
while True:
    if len(primes) == 10001:
        break

    if isPrime(num):
        primes.append(num)
    
    num += 1

print(primes[-1])