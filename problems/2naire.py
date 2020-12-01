import random
import math
cases = []
while True:
    n,t = [float(x) for x in input().split()]
    if n == 0 and t == 0:
        break
    else:
        e = []
        for j in range(0,10):
            tc = 1
            for i in range(0,int(n)):
                p = random.uniform(t,1)
                tc = tc*p
                print(tc,i,2**i)
            e.append(tc*(2**(int(n)+1)))
        else:
            cases.append(e)

for i in cases:
    print(i)
        #print(sum)
