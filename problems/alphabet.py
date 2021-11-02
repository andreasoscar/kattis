def lcs(x,y,m,n):
    matrix = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            else:
                if x[i-1] == y[j-1]:
                    matrix[i][j] = 1 + matrix[i-1][j-1]
                else:
                    matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    return matrix

match = "abcdefghijklmnopqrstuvwxyz"
s = input()
vlist = lcs(s,match,len(s),len(match))
print(26-max(vlist[len(vlist)-1]))