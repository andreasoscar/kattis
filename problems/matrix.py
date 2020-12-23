import sys
matrix,temp,i = [],[],1
for k in sys.stdin:
    if k != "\n" or '':
        temp.append([int(v) for v in k.rstrip().split(" ")])
    if len(temp) == 2:
        matrix.append(temp)
        temp = []
for j in matrix:
    determinant = 1/(j[0][0]*j[1][1] - j[0][1]*j[1][0])
    t,b = j[0],j[1]
    print("Case " + str(i) + ":")
    print(str(int(b[1]*determinant)) + " " + str(int(-t[1]*determinant)))
    print(str(int(-b[0]*determinant)) + " " + str(int(t[0]*determinant)))
    i += 1
