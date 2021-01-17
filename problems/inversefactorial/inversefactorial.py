#!/usr/bin/python3
# problem: inversefactorial, rating: 5.5
import math
from decimal import Decimal
n = int(input())
k = str(n)
if len(k) < 6 and n < 40320:
    s = dict()
    s[0] = s[1] = 1
    fact = 1
    for i in range(2,10):
        fact = fact * i
        s[fact] = i
    print(s[n])
else:
    res = 0
    for i in range(1,1000000):
        res += math.log10(i)
        if int(res)+1==len(k):
            print(i)
            break
