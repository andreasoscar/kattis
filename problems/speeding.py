n = int(input())
values = []
for i in range(n):
    i,k = [int(_) for _ in input().split()]
    values.append((i,k))
m = -1
for i in range(0,len(values)-1):
    if (values[i+1][1] - values[i][1])/(values[i+1][0] - values[i][0]) > m:
        m = int((values[i+1][1] - values[i][1])/(values[i+1][0] - values[i][0]))
print(m)
