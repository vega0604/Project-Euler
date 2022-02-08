
def genTriangleNum(num):
    triangle = 0

    for x in range(1, num+1):
        triangle += x

    return triangle

def getFactors(num):
    factors = []

    for factor in range(1, round(num**0.5)+1):
        if num % factor == 0:
            factors.append(factor)

    return factors

current = 1
while True:
    triangleNum = genTriangleNum(current)

    factors = getFactors(triangleNum)
    if len(factors) * 2 > 500:
        break

    current += 1

print(triangleNum)