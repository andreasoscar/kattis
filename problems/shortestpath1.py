from collections import deque
INF = float('inf')
def dijkstras(graph,source):
    Q = set()
    dist = [INF]*len(graph[source])
    print(graph)

    while Q:
        u,min = -1,INF
        for node in Q:
            if dist[node] < min:
                min = dist[node]
                u = node
        if u == -1:
            return dist
        Q.remove(u)
        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
    return dist
while True:
    n,m,q,s = [int(_) for _ in input().split()]
    if n == 0 and m == 0 and q == 0 and s == 0:
        break
    else:
        matrix = dict()
        for edge in range(m):
            u,v,w = [int(_) for _ in input().split()]
            if u in matrix.keys():
                matrix[u] = matrix[u] + [v,w]
            else:
                matrix[u] = [v,w]
        n = dijkstras(matrix,s)
        for edge in range(q):
            target = int(input())
            w = n[target]
            if w == INF:
                print("Impossible")
            else:
                print(w)
        print()
