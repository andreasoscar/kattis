from sys import stdin
L = []
ints = []
def summation(k):
    suma = 0
    for c in k.rstrip():
        suma += int(c)
    return suma

for line in stdin:
    if line.rstrip() == "0":
        break
    else:
        ints.append(line.rstrip())

for k in ints:
    incr = 11
    while(incr > 10 and not summation(k) == summation(str(int(k) * incr))):
        incr += 1
    L.append(incr)

for k in L:
    print(k)
