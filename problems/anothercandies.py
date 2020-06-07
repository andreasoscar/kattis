entry = int(input())
bools = []
i = 0
n = 0
sum = 0
while i <= entry:
    c = input()
    if c == "":
        i += 1
        n = 0
        sum = 0
    else:
        n = int(c)
        for v in range(n):
            inx = input()
            if not inx == "":
                sum += int(inx)
        if sum % n == 0:
            bools.append("YES")
        else:
            bools.append("NO")
        if i == entry:
            break
for k in bools:
    print(k)
