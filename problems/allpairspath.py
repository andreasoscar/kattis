inf = float('inf')
inf1 = -inf
def warshall(G):
    d,t = G,len(G)

    #print(d,t)
    for i in range(t):
        for j in range(t):
            for k in range(t):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    # for i in range(t):
    #     for j in range(t):
    #         for k in range(t):
    #             if d[k][k] < 0 and d[i][k] != inf and d[k][j] != inf:
    #                 d[i][j] = inf1
    return d

while True:
    n,m,q = [int(i) for i in input().split(" ")]
    if n == 0 and m == 0 and q == 0:
        break
    else:
        edges,dir,g = [],[],set()
        for i in range(m):
            s,t,c = [int(i) for i in input().split()]
            edge = [inf]*(n+1)
            edge[t] = c
            edges.insert(i,edge)
            g.add(s)
        for v in set(range(0,n)).difference(g):
            edges.insert(v,[inf]*(n+1))
        for j in range(q):
            s,t = [int(i) for i in input().split()]
            dir.append([s,t])
        sp = warshall(edges)
        for v in dir:
            s,t = v[0],v[1]
            if s < len(sp) and t < len(sp):
                if s == t:
                    print(0)
                elif sp[s][t] == inf:
                    print("Impossible")
                elif sp[s][t] == inf1:
                    print("-Infinity")
                else:
                    print(sp[s][t])
        print("\n")
