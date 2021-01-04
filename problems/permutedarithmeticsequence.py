n = int(input())
for j in range(n):
    seq = [int(y) for y in input().split()[1:]]
    s = sorted(seq)
    d = seq[1] - seq[0]
    a,pa = True,True
    for y in range(1,len(seq)-1):
        if seq[y+1] - seq[y] != d:
            a = False
            break
    d = s[1] - s[0]
    for y in range(1,len(s)-1):
        if s[y+1] - s[y] != d:
            pa = False
            break
    if a:
        print("arithmetic")
    elif pa:
        print("permuted arithmetic")
    else:
        print("non-arithmetic")