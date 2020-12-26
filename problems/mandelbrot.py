import cmath
import sys
i = 1
for lin in sys.stdin:
    x,y,r = [float(i) for i in lin.split()]
    c,f = complex(x,y),True
    z_n = 0
    while r > 0:
        z_n1 = z_n**2 + c
        z_n = z_n1
        if abs(z_n) > 2:
            f = False
            break
        r -= 1
    if f:
        print("Case " + str(i) + ": IN")

    else:
        print("Case " + str(i) + ": OUT")
    i += 1
