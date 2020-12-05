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
        newDist = []
        for i in dist.items():
            if i[0] in Q:
                newDist.append(i)
        min = float('inf')
        u = -1
        for i in newDist:
            if min > i[1] and i[0] in neighbors.keys():
                min = i[1]
                u = i[0]
        if u == -1:
            break
        elif u >= 0:
            Q.remove(u)
            for i in neighbors[u]:
                if i in Q:
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
        neighbors = dict()
        paths = dict()
        queries = []
        for i in range(m):
            s,t,c = [int(i) for i in input().split(" ")]
            paths[(s,t)] = c
            if s in neighbors.keys():
                neighbors[s] = neighbors[s] + [t]
            else:
                neighbors[s] = [t]
        for j in range(q):
            s,t = [int(i) for i in input().split(" ")]
            queries.append([s,t])
        for i in queries:
            ways = dijkstra(paths,i[0],neighbors)
            if i[1] not in ways.keys() or ways[i[1]] == 'inf':
                print("Impossible")
            else:
                print(ways[i[1]])
        print("\n")
