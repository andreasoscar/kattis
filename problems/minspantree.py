
from collections import defaultdict
import heapq
import sys
def prim(G, r):
    totWeight = 0
    edges = dict()
    V = set()  # visited
    Q = [(0, r)]  # not visited
    while Q:
        weight, v = heapq.heappop(Q)
        if v not in V:
            V.add(v)
            totWeight += weight
            for u, w in G[v]:
                if u not in V:
                    heapq.heappush(Q, (w, u))
                    edges[u] = v



    if totWeight == 0:
        return -1,edges
    else:
        return totWeight,edges

while True:
    n,m = [int(x) for x in input().split(' ')]
    if n == 0 and m == 0:
        break
    else:
        graph = defaultdict(list)
        for i in range(m):
            temp = input().split(' ')
            first, second, cost = int(temp[0]), int(temp[1]), int(temp[2])
            graph[first].append((second, cost))
            graph[second].append((first, cost))
        cost,edges = prim(graph,0)
        if cost == -1:
            print("Impossible")
        else:
            print(cost)
            for i in edges.items():
                print(str(i[1]) + " " + str(i[0]))
