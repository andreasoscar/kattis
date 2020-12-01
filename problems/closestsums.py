
import fileinput
k = []
for line in fileinput.input():
    k.append(int(line))
r = 0
n,m = k[0],k[k[0]+1]
r = n+m
ml = []
nl = []
nms = []
nms.append((n,m))
sumn = nms[0][0]
summ = nms[0][1]
for i in range(1,len(k)):
    if i == r+2:
        n,m = k[i],k[k[i]+1+i]
        r = r + n + m + 2
        nms.append((n,m))
r1 = 0
for i in nms:
    nl.append(k[1+r1:(i[0]+1+r1)])
    ml.append(k[(2+i[0]+r1):(i[0]+i[1]+2+r1)])
    r1 = r1 + i[0]+i[1]+2
finalList = []

r2 = 0
for x in ml:
    tempList = []
    for i in x:
        closest = 1000000000
        carry = 1000000000
        for j in range(0,len(nl[r2])):
            for t in range(0,j):
                if not nl[r2][j] == nl[r2][t]:
                    if nl[r2][j]+nl[r2][t] == i:
                        closest = nl[r2][j]+nl[r2][t]
                        carry = closest
                        closest = 0
                        break
                    elif abs(nl[r2][j]+nl[r2][t] - i) <= closest:
                        closest = abs(nl[r2][j]+nl[r2][t] - i)
                        carry = nl[r2][j]+nl[r2][t]
        tempList.append(carry)
    finalList.append(tempList)
    r2 = r2 + 1
t1 = 0
for i in range(0,len(finalList)):
    print("Case " + str(1 + t1) + ":")
    for j in range(0,len(ml[i])):
        print("Closest sum to " + str(ml[i][j]) + " is " + str(finalList[i][j]) + ".")
    t1 = t1 + 1
