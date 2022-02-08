num = 10000

def sumOfDivisors(n):
    total = 0

    for x in range(1, n//2+1):
        if n % x == 0:
            total += x

    return total

total = 0
for i in range(1, num+1):
    divisors = sumOfDivisors(i)
    divisors2 = sumOfDivisors(divisors)
    # print(f'current: {i}')
    # print(f'divisors: {divisors}')
    # print(f'divisors2: {divisors2}')
    if divisors == divisors2 and i != divisors:
        total += divisors + i

print(total)
