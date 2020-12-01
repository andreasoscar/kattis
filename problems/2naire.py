import random
import math
cases = []
while True:
    n,t = [float(x) for x in input().split()]
    if n == 0 and t == 0:
        break
    else:
        i_t = []
        for j in range(0,100000):
            money = 1
            for i in range(0,int(n)):
                p = random.uniform(t,1)
                if 1-p > p:
                    break
                else:
                    money = money*2*p
            i_t.append(money)
        cases.append(sum(i_t)/len(i_t))
for i in cases:
    print(round(i,3))
