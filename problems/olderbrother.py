import math
from bitarray import bitarray

q = int(input())

def primesieve(n):
    prime = bitarray(n+1)
    prime.setall(False)
    for i in range(2,int(math.sqrt(n))+1):
        if prime[i]:
            for j in range(i+i,n+1,2*i):
                prime[j] = False
    return prime

def uniquepowerprime(n):
    count = 0
    primes = primesieve(n)
    if n > 1:
        if primes[n]:
            return 1
        for i in range(2,n):
            if primes[i]:
                if n%i==0:
                    while n%i==0:
                        n = n//i
                        count += 1
                    if n == 1:
                        return count
                    return 0
    return 0
print(primesieve(q))
            

