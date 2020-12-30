from collections import Counter
N,t = [int(y) for y in input().split()]
A = [int(y) for y in input().split()]
if t == 1:
    s = "No"
    for i in A:
        if i + 7777-i == 7777 and i != 7777-i:
            s = "Yes"
    print(s)
elif t == 2:
    if len(A) == len(set(A)):
        print("Unique")
    else:
        print("Contains duplicate")
elif t == 3:
    v = -1
    z = Counter(A)
    for i in A:
        if z[i] > N//2:
            v = i
            break
    print(v)
elif t == 4:
    A.sort()
    if N % 2 == 1:
        print(A[(len(A)//2)])
    else:
        print(str(A[(len(A)//2)-1]) + " " + str(A[(len(A)//2)]))
elif t == 5:
    A.sort()
    for i in A:
        if i >= 100 and i <= 999:
            print(str(i) + " ",end='')
