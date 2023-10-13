import math
n = int(input())
l = list()
i = 1

while i <= math.sqrt(n):
    if n%i==0 :
        l.append(i)
        if i != (n//i):
            l.append((n//i))
    i += 1

for k in sorted(l):
    print(k)