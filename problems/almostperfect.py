import fileinput
import math
v = []
for line in fileinput.input():
    if line != "\n":
        v.append(int(line.replace("\n","")))
for k in v:
    divs = set()
    divs.add(1)
    for i in range(1,math.ceil(math.sqrt(k))+1):
        if k % i == 0:
            if i > 1:
                divs.add(int(k/i))
                divs.add(int(i))
    if k == sum(divs):
        print(str(k) + " perfect")
    elif abs(k - sum(divs)) <= 2:
        print(str(k) + " almost perfect")
    else:
        print(str(k) + " not perfect")
