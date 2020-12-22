while True:
    z = input()
    if z == '0':
        break
    else:
        x1,y1,x2,y2,p = [float(x) for x in z.split()]
        print("{:.10f}".format((abs(x1-x2)**p+abs(y1-y2)**p)**(1/p)))
