import itertools
n = input()
possible = []
for i in itertools.permutations(n, len(n)):
    col = ""
    for j in range(len(n)):
        col = col + i[j]
    possible.append(int(col))
del possible[0]
t = [x for x in possible if x > int(n)]
if len(t) == 0:
    print(0)
else:
    print(min(t))
