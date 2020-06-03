import sys
pairs = []
for line in sys.stdin:
    pairs.append(tuple((int(line.split(' ')[0]),int(line.split(' ')[1]))))

for i in pairs:
    print(abs(i[0]-i[1]))
