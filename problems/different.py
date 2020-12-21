import sys
for i in sys.stdin:
    i = i.split()
    print(abs(int(i[1])-int(i[0])))
