n = int(input())
for i in range(n):
    c = int(input())
    nbrs = []
    for j in range(c):
        nbrs.append(input())
    nbrs.sort(key=lambda s: len(s))
    print(nbrs)
