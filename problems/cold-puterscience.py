i = 0
N = int(input()) #totally unnecessary
L = input().split(' ')
for k in L:
    if int(k) < 0:
        i += 1
print(i)
