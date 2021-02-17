n,s=-1,-1
for i in range(5):
    z = [int(x) for x in input().split(" ")]
    if sum(z) > s:
        s = sum(z)
        n = i+1
print(n,s)
