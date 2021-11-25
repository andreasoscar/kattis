a,b,c,d,e = [int(x) for x in input().split()]
v = int(input())
if a <= v:
    print("A")
elif b <= v:
    print("B")
elif c <= v:
    print("C")
elif d <= v:
    print("D")
elif e <= v:
    print("E")
else:
    print("F")