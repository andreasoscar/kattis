n,d = [int(y) for y in input().split()]
a = [int(y) for y in input().split()]
for i in range(len(a)):
    for j in range(0,i):
        if a[i]//d == a[j]//d:
            nbr += 1
print(nbr)
