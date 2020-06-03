sum = 0
for k in range(int(input())):
    x = input().split(' ')
    sum += float(x[0]) * float(x[1])
print(round(sum,4))
