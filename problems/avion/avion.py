#!/usr/bin/python3
# problem: avion, rating: 1.4
import sys
k = 0
x = False
for i in sys.stdin:
    k += 1
    if "FBI" in i:
        print(k, sep=' ', end=" ",flush=True)
        x = True
if not x:
    print("HE GOT AWAY!")
