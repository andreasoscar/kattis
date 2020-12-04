t = int(input())
imp = []
while t > 0:
    imports = 0
    z = [int(i) for i in input().split(" ")]
    for i in range(0,len(z)-1):
        if z[i+1]/z[i] > 2:
            imports += z[i+1] - (z[i]*2)
    t = t - 1
    imp.append(imports)
for i in imp:
    print(i)
