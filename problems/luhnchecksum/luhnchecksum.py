#!/usr/bin/python3
# problem: luhnchecksum, rating: 1.6
for i in range(int(input())):
    z = [int(y) for y in input()]
    for i in range(len(z)-2,-1,-2):
        if z[i]*2 > 9:
            z[i] = z[i]*2 - 9
        else:
            z[i] = z[i]*2
    if sum(z) % 10 == 0:
        print("PASS")
    else:
        print("FAIL")
