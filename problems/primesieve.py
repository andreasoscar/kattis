import math
n,q = [int(y) for y in input().split()]
ins = []
for j in range(q):
    ins.append(int(input()))
p = [True]*(n+1)
v = 0
p[0] = p[1] = False
for i in range(2,int(math.sqrt(n))+1):
    if p[i]:
        for j in range(i*i,n+1,i):
            p[j] = False
for k in range(2,n+1):
    if p[k]:
        v += 1
print(v)
for j in ins:
    if p[j]:
        print(1)
    else:
        print(0)
