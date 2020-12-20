z = input().split(';')
total = 0
for y in z:
    if "-" in y:
        x = y.split("-")
        total += (int(x[1]) - int(x[0]) + 1)
    else:
        total += 1
print(total)
