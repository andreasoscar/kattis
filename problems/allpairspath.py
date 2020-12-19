INF = float('inf')
def warshall(G,t):
    for i in range(t):
        for j in range(t):
            for k in range(t):
                if G[j][i] < INF and G[i][k] < INF:
                    G[j][k] = min(G[j][k],G[j][i] + G[i][k])
    for i in range(t):
        for j in range(t):
            for k in range(t):
                if G[i][j] != -INF:
                    if G[k][k] < 0 and G[i][k] != INF and G[k][j] != INF:
                        G[i][j] = -INF


while True:
    n,m,q = [int(i) for i in input().split(" ")]
    if n == 0 and m == 0 and q == 0:
        break
    else:
        matrix = [[0 if i == j else INF for i in range(n)] for j in range(n)]
        for i in range(m):
            s,t,c = [int(_) for _ in input().split()]
            if s == t:
                matrix[s][t] = 0
            elif matrix[s][t] > c:
                matrix[s][t] = c
        warshall(matrix,n)
        for j in range(q):
            s,t = [int(_) for _ in input().split()]
            c = matrix[s][t]
            if c == -INF:
                print("-Infinity")
            elif c == INF:
                print("Impossible")
            else:
                print(c)
        print()
