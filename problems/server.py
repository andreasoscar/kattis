n,T = [int(i) for i in input().split(" ")]
tasks = [int(i) for i in input().split(" ")]
tr = 0
for k in tasks:
    if T - k >= 0:
        T = T - k
        tr += 1
    else:
        break
print(tr)
