
product = 0

for a in range(1, 1001):
    for b in range(a+1, 1001):
        c = (a**2 + b**2)**0.5

        if a + b + c == 1000:
            product = a*b*c

print(product)