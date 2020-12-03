import math
k = int(input())
for i in range(k):
    v0,theta,x1,h1,h2 = [float(x) for x in input().split()]
    theta = theta*(math.pi/180)
    t1 = x1/(v0*math.cos(theta))
    y1 = v0*t1*math.sin(theta) - ((1/2)*9.81*(t1**2))
    if y1-1 > h1 and y1+1 < h2:
        print("Safe")
    else:
        print("Not Safe")
