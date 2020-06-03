import math
X = int(input())

def findClosestPrimeFactors(y):
    inside = []
    if y % 2 == 0:
        #divisble by 2, prime
        inside.append(2)
        y = y / 2
    for i in range(3, int(math.sqrt(y))+1,2):
        while y % i == 0:
            inside.append(i)
            y = y / i
    if y >= 2:
        inside.append(int(y))
    return inside

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def fillList(p):
    temp = []
    temp.append(p)
    f = False
    holdList = temp.copy()
    while not f:
        if not all(isPrime(k) for k in temp):
            for k in temp:
                if not isPrime(k):
                    v = findClosestPrimeFactors(k)
                    temp.remove(k)
                    holdList = temp +  v
                    temp = holdList.copy()
        else:
            f = True
            return temp
    return temp
print(len(fillList(X)))
