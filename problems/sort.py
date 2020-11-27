n,k = [int(t) for t in input().split()]
list = dict()
inputs = [int(t) for t in input().split()]
for z in inputs:
    if not z in list.keys():
        list[z] = 1
    else:
        list[z] = list[z] + 1
list = dict(sorted(list.items(),key=lambda k:k[1],reverse=True))
for i in list:
    for k in range(0,list[i]):
        print(str(i) + " ",end='')
