import math
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
A = [True]*(78498)
A[0] = A[1] = False
for i in range(2,int(math.sqrt(78498))+1):
    if A[i]:
        for j in range(i**i,78498,i):
            A[j] = False
for j in data:
    prod = 1
    primes = []
    if j > 1:
        for i in range(len(A)):
            if A[i]:
                if len(str(prod)) < j and len(primes) >= j:
                    del primes[0]
                elif len(str(prod*i)) <= j:
                    primes.append(i)
                    prod = prod * i
                elif len(str(prod)) == j:
                    break
        print(*primes)
    else:
        print("5")
