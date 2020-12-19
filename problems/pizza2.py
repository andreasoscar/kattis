import math
r,c = [int(_) for _ in input().split()]
inner = ((r-c)**2)*math.pi
outer = ((r)**2)*math.pi
if r == c:
    print(0)
else:
    print("{:.6f}".format(100*inner/outer));
