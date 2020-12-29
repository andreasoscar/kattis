import math
n,q = [int(y) for y in input().split()]
ins = []
for j in range(q):
    ins.append(int(input()))
def sieve(n):
    p = [True]*(n+1)
    p[0] = p[1] = False
    for i in range(2,int(math.sqrt(n)+1)):
        if p[i]:
            for j in range(i*i,n+1,i):
                p[j] = False
    return p
primes = sieve(n)
v = 0
for k in range(n+1):
    if primes[k]:
        v += 1
print(v)
for j in ins:
    if primes[j]:
        print(1)
    else:
        print(0)
