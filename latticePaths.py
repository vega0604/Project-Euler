def factorial(num):

    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

n = k = 20

n += 20

c = factorial(n) / (factorial(n-k) * factorial(k))
print(c)