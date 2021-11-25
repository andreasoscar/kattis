i,j,k = input().split(),input().split(),input().split()
x = [i[0],j[0],k[0]]
y = [i[1],j[1],k[1]]
countsx = dict()
for i in x:
  countsx[i] = countsx.get(i, 0) + 1
countsy = dict()
for i in y:
  countsy[i] = countsy.get(i, 0) + 1
sortedx = sorted(countsx.items(), key=lambda item: item[1])
sortedy = sorted(countsy.items(), key=lambda item: item[1])
print(sortedx[0][0],sortedy[0][0])