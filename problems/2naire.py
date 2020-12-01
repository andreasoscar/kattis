import random
import math
cases = []
while True:
    n,t = [float(x) for x in input().split()]
    if n == 0 and t == 0:
        break
    else:
        i_t = []
        for l in range(0,2):
            chances = []
            recurringFac = 1
            w = 1
            for i in range(0,int(n)):
                chances.append(random.uniform(t,1))

            for h in range(1,len(chances)):
                w = w + recurringFac*chances[h]*2**(h)
                recurringFac = recurringFac*chances[h]
                #print(recurringFac,2**(h))
            i_t.append(w)
        #    print(w)
    #        print(w)
        cases.append(sum(i_t)/len(i_t))
for i in cases:
    print(round(i,3))


# w = math.sqrt(((1-t)**2)/12)
# print(w)
# for j in range(0,1000):
#     money = 1
#     for i in range(0,int(n)):
#         p = random.uniform(t,1)
#
#         if 1-p > p:
#             break
#         else:
#             money = money*2*p
#     i_t.append(money)
# cases.append(sum(i_t)/len(i_t))
