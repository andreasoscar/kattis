x = int(input())
sum = 0
facs = []
for i in range(0,x+1):
    if(len(facs) == 0):
        facs.append(1)
    else:
        facs.append(facs[i-1]*i)
    if(i > 1):
        sum += (1/(i*facs[i-1]))
    else:
        sum += 1
print(sum)
