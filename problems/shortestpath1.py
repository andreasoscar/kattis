from collections import deque
inf = float('inf')
def dijkstras(graph,source,nodes):
    Q = set()
    dist = [0 for i in range(nodes)]
    prev = [None for i in range(nodes)]
    for i in range(nodes):
        dist[i] = inf
        Q.add(i)
    dist[source] = 0

    while Q:
        print("loop")
        u = dist.index(min(dist))
        
        Q.remove(u)
        filtered = filter(lambda edge: edge[0] == u and edge[1] in Q, graph)
        for i in filtered:
            alt = dist[u] + i[2]
            if alt < dist[i[1]]:
                dist[i[1]] = alt
                prev[i[1]] = u
    return dist,prev

graph,queries = [], []
current = False
source = ""
nodes = -1
while True:
    s = input()
    if s == "0 0 0 0":
        break
    else:
        s = s.split()
        if len(s) == 4 and not current:
            source = int(s[3])
            nodes = int(s[0])
            current = True
        if len(s) == 4 and current:
            graph = []
            queries = []
        if len(s) == 1 and current:
            queries.append(s)
        if len(s) == 3 and current:
            graph.append((int(s[0]),int(s[1]),int(s[2])))
    
dijkstras(graph,source,nodes)

            

    

