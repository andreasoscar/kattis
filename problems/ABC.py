import sys
data = []
for line in sys.stdin:
    data.append(line.rstrip())

integers = sorted(map(int, data[0].split(' ')))
bindings = dict(zip(('A','B','C'), integers))
completeList = []

for k in data[1]:
    completeList.append(bindings.get('' + k + ''))

print(" ".join(str(y) for y in completeList))
