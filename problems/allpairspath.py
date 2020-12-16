inf = float('inf')
import copy
def warshall(G,k):
    print(G)
    distance = copy.copy(G)
    for i in range(k):
        for j in range(k):
            for v in range(k):
                distance[j][v] = min(distance[j][v],distance[j][i] + distance[i][v])
    return distance

while True:
    n,m,q = [int(i) for i in input().split(" ")]
    if n == 0 and m == 0 and q == 0:
        break
    else:
        sy = set()
        graph,queries = [[inf,inf,inf,inf]]*n,[]
        for i in range(m):
            s,t,c = [int(i) for i in input().split()]
            graph[s].insert(t,c)
        paths = (warshall(graph,len(sy)))
        for i in range(q):
            s,t = [int(_) for _ in input().split()]
            if paths[s][t] == inf:
                print("Impossible")
            else:
                if s == t:
                    print(0)
                else:
                    print(paths[s][t])
        print("\n")
