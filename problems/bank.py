f = input().split()
values = []
list = []
time = 0
sum = 0
for i in range(int(f[0])):
    k = input().split()
    values.append((int(k[0]), int(k[1])))
co = values.copy()
co.sort(key=lambda x: x[1])
for c in co:
    (v,i) = c
    if int(f[1]) > time and i >= time:
        time += 1

print(sum)
