sumSquare = sum([x**2 for x in range(1, 101)])
squareSum = sum(range(1, 101))**2

diff = squareSum - sumSquare
print(diff)