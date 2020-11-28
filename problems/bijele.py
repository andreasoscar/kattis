list = [1,1,2,2,2,8]
print(' '.join(str(e) for e in [x1-x2 for (x1,x2) in zip(list,[int(t) for t in input().split()])]))
