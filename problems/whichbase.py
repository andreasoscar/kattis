import math
itr = int(input())
list = []
for k in range(itr):
    list.append((input().split(' ')))
p = 1
for k in list:
    try:
        print(p,int(k[1],8),int(k[1]),int(k[1],16))
        p += 1
    except:
        print(p,int(0),int(k[1]),int(k[1],16))
        p += 1
