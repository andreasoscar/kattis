l,x = [int(x) for x in input().split()]
t,r = 0,0
for i in range(0,x):
    z = input().split()
    if z[0] == "enter" and t + int(z[1]) <= l:
        t = t + int(z[1])
    elif z[0] == "leave":
        t = t - int(z[1])
    else:
        r = r + 1
print(r)
