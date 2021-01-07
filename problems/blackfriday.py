n,y = input(),[int(i) for i in input().split()]
h = y
y = sorted([i for i in y if y.count(i) == 1],reverse=True)
if len(y) == 0:
    print("none")
else:
    print(h.index(y[0])+1)
