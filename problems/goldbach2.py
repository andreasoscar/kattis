import sys
import math
ins = []
for i in sys.stdin:
    ins.append(int(i))
del ins[0]
def sieve(n):
    p = [True]*(n+1)
    p[0] = p[1] = False
    for i in range(2,int(math.sqrt(n)+1)):
        if p[i]:
            for j in range(i**2,n+1,i):
                p[j] = False
    return p
primes = sieve(max(ins)+1)
def find(v):
    possible = []
    for j in range(2,v//2+1):
        if primes[j] and primes[v-j]:
            if not (v-j,j) in possible and not (j,v-j) in possible:
                possible.append((j,v-j))
    return possible

for i in ins:
    y = find(i)
    if len(y) > 0:
        print(str(i) + " has " + str(len(y)) + " representation(s)")
        for j in y:
            print(str(j[0]) + "+" + str(j[1]))
        print("")
