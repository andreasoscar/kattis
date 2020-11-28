n,m = [int(x) for x in input().split()]
c = dict()
list = []
for i in range(1,n+1):
    for j in range(1,m+1):
        sum = i+j
        if not sum in c.keys():
            c[sum] = 1/(n**2)
        else:
            c[sum] = c[sum] + 1/(n**2)
ma = c[max(c,key=c.get)]
for i in c:
    if c[i] == ma:
        list.append(i)
for i in list:
    print(i)
