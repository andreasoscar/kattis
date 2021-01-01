import math
n = int(input())
v = 78498
data = []
for i in range(n):
    data.append(int(input()))
A = [True]*(v+1)
A[0] = A[1] = False
for i in range(2,int(math.sqrt(v+1))+1):
    if A[i]:
        for j in range(i*2,v+1,i):
            A[j] = False
for j in data:
    prod = 1
    primes = []
    if j > 1:
        i = 0
        while len(str(prod)) < j:
            if len(primes) == j-1 and len(str(prod*i)) < j:
                del primes[0]
            elif A[i]:
                prod = prod * i
                primes.append(i)
                i += 1
            else:
                i += 1
        print(*primes)
    elif j == 1:
        print("3")
