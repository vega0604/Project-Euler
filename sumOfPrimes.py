
def primes(limit):
    primes = []
    for num in range(2, limit+1):
        isPrime = True
        for factor in range(2, round(num**0.5)+1):
            if num % factor == 0:
                isPrime = False

        if isPrime:
            primes.append(num)

    return primes

print(sum(primes(2000000)))