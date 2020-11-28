c = float(input())
l = float(input())
cost = 0
m = []
while l > 0:
    m.append([float(t) for t in input().split()])
    l = l - 1
for i in m:
    cost = cost + c*((i[0])*(i[1]))
print(cost)
