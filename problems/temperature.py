x,y = [int(t) for t in input().split(" ")]
ta = 0
tb = x
x1 = 0
if x == 0 and y == 1:
    print("ALL GOOD")
elif y > 1:
    if abs(x) == abs(y):
        print("Impossible")
    else:
        x1 = x/(y-1)
        print(x1,y*x1)
        tb = tb - y*x1
        print(float(tb))
else:
    print("här")
    if x != 0:
        print("Impossible")
