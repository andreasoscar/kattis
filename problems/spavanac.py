h,m = [int(i) for i in input().split(" ")]
if m-45 < 0:
    if h-1<0:
        h = 23
    else:
        h = h - 1
    m = 60 - (45-m)
else:
    m = m - 45
print(h,m)
