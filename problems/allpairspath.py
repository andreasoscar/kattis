from datetime import datetime
import sys
def dijkstra(graph,source,neighbors):
    Q = set()
    dist = dict()
    prev = dict()
    for i in graph:
        u,v = i[0],i[1]
        dist[v] = float('inf')
        prev[v] = -1
        Q.add(u)
        Q.add(v)
    dist[source] = 0
    while len(Q) > 0:
        newDist = dict()
        for i in dist.items():
            if i[0] in Q:
                newDist[i[0]] = i[1]
        if len(newDist) == 0:
            break
        u = min(newDist,key=newDist.get)
        Q.remove(u)
        for i in neighbors[u]:
            dis = dist[u] + graph[(u,i)]
            if dis < dist[i]:
                dist[i] = dis
                prev[i] = u
    return dist
while True:
    n,m,q = [int(i) for i in input().split(" ")]
    if n == 0 and m == 0 and q == 0:
        break
    else:
        neighbors = [[]]*n
        paths = dict()
        queries = []
        for i in range(m):
            s,t,c = [int(i) for i in input().split(" ")]
            paths[(s,t)] = c
            neighbors[s] = neighbors[s] + [t]
        for j in range(q):
            s,t = [int(i) for i in input().split(" ")]
            queries.append([s,t])
        ways = dijkstra(paths,0,neighbors)
        for i in queries:
            if i[0] == i[1]:
                print("0")
            elif i[0] == 0 and i[1] in ways:
                print(ways[i[1]])
            elif i[0] != 0:
                if (i[0],i[1]) in paths and i[1] in ways:
                    print(abs((ways[i[1]] - paths[(i[0],i[1])])))
                else:
                    print("Impossible")
        print("\n")
