import math
nbr = int(input())
points = []
for i in range(nbr):
    inp = input().split(' ')
    points.append(tuple((int(inp[0]), int(inp[1]))))

iY = 0
iX = 0
sumX = 0
sumY = 0
for i in points:
    iY += 1
    iX += 1
    sumX += i[0]
    sumY += i[1]

print(sumY/iY - sumX/iX)
