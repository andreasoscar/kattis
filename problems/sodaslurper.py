e,f,c = [int(_) for _ in input().split()]
tot = e+f
d = 0
while True:
    d += int(tot/c)
    tot = tot%c + int(tot/c)
    if tot < c:
        break
print(d)
