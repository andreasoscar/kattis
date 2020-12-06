import math
from itertools import permutations
z = int(input())
def isPrime(n):
    if n > 1:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
                break
        return True
    else:
        return False

for i in range(0,z):
    total = 0
    t = input()
    v = set()
    for j in range(1,len(t)+1):
        for p in permutations(str(t),j):
            p = "".join(p)
            v.add(int(p))
    for i in v:
        if isPrime(i):
            total += 1

    print(total)
