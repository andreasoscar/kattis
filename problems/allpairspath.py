inf = float('inf')
import copy
def warshall(G,t):
    d = copy.deepcopy(G)
    print(d.keys())
    for c in G:
        for j in d.keys():
            if not j in d[c].keys():
                if c == j:
                    d[c].update({c:0})
                else:
                    d[c].update({j:inf})
    print(d)
    for i in range(t):
        for j in range(t):
            for k in range(t):
                print(d)
                print(i,j,k)
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    # for i in range(t):
    #     for j in range(t):
    #         for k in range(t):
    #             if d[k][k] < 0 and d[i][k] != inf and d[k][j] != inf:
    #                 d[i][j] = -inf
#    return d

while True:
    n,m,q = [int(i) for i in input().split(" ")]
    if n == 0 and m == 0 and q == 0:
        break
    else:
        pairs,dir = dict(),[]
        for i in range(m):
            s,t,c = [int(i) for i in input().split()]
            tmp = dict()
            if s in pairs.keys():
                tmp[t] = c
                pairs[s] = pairs[s] + tmp
            else:
                tmp[t] = c
                pairs[s] = tmp
        for i in range(q):
            s,t = [int(i) for i in input().split()]
            dir.append([s,t])
        print(warshall(pairs,len(pairs)))
