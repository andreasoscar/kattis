import math
ins = []
def near(n):
    prime_near = 0
    for i in range(n+1,2*n):
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            prime_near = i
            break
    return prime_near
def isPrime(n):
    if n > 1:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        return False

while True:
    k = int(input())
    if k == 0:
        break
    else:
        ins.append(k)

for i in ins:
    ct = near(2*i)
    if isPrime(i):
        print(ct)
    else:
        print(str(ct) + " (" + str(i) + " is not prime)")
