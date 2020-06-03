import sys
import math
ite = int(input())
nbrs = []

for i in range(ite):
    nbrs.append(int(input()))

for k in nbrs:
    length = len(str(math.factorial(k)))-1
    print(str(math.factorial(k))[length])
