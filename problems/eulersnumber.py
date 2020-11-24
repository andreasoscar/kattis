x = int(input())
sum = 1
facs = [1]
for i in range(1,x+1):
    facs.append(facs[i-1]*i)
    if(i > 1):
        sum += (1/(i*facs[i-1]))
    else:
        sum += 1
print(sum)
