from math import sqrt

n, w, h = [int(i) for i in input().split(" ")]
diagonal = sqrt(w*w+h*h)

inp = list()
for i in range(n):
    inp.append(int(input()))

for i in inp:
    if(i > diagonal):
        print("NE")
    else:
        print("DA")

