n = int(input())
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append([''])
for i in range(n):
    a = input()
    for j in range(len(a)):
        matrix[i][j] = a[j]
