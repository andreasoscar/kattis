import math
v = input().split(' ')
values = []
p = int(v[0])
a = int(v[1])
b = int(v[2])
c = int(v[3])
d = int(v[4])
nBound = int(v[5])
tradingPrice = []
majorDiff = 0
curPos = 0

def func(k):
    return p * (math.sin(a * k + b) + math.cos(c*k+d)+2)

for i in range(nBound):
    tradingPrice.append(func(i+1))

for i in tradingPrice:
    pivot = tradingPrice[curPos]
    if pivot - i < 0 and not (pivot == i):
        curPos = tradingPrice.index(i)
    elif pivot - i > majorDiff and not (pivot == i):
        majorDiff = pivot - i

if majorDiff > 0:
    print(majorDiff)
else:
    print("0")
