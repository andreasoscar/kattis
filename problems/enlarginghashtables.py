import math
ins = []
i = 0
def generatePrimes(n):
  primes = [True] * (2*(n+1))
  for p in range(2, n+1):
    if (primes[p]):
      for i in range(p, n+1, p):
        primes[i] = False
  return primes

while True:
    k = int(input())
    if k == 0:
        break
    else:
        ins.append(k)

allPrimes = generatePrimes(max(ins))
print(ins)

for i in ins:
    if 2*i >= 6:
        factor = round(2*i/6)
        if allPrimes[factor*6 + 1]:
            print(factor*6 + 1)
        elif allPrimes[factor*6 - 1]:
            print(factor*6 - 1)
        else:
            factor += 1
