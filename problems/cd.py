while True:
    n,m = [int(i) for i in input().split()]
    if n == 0 and m == 0:
        break
    j,k = set(),set()
    for i in range(n):
        j.add(int(input()))
    for i in range (m):
        k.add(int(input()))
    print(len(j.intersection(k)))
