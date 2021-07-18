p,t = [int(i) for i in input().split()]
totalSolved = 0
for i in range(p):
    solved = 0
    for j in range(t):
        z = input()
        if z.lower() == z[0].lower() + z[1:]:
            solved += 1
    if solved == t:
        totalSolved += 1
print(totalSolved)
