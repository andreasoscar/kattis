x,y = [int(t) for t in input().split(" ")]
ta = 0
tb = x
if x == 0 and y == 1:
    print("ALL GOOD")
elif y == 1 and x != 0:
    print("Impossible")
else:
    if x == y:
        print("Impossible")
    else:
        x1 = (ta-tb)/(1-y)
        ta = ta - x1
    print(ta)
