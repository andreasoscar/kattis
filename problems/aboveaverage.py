e = int(input())
for i in range(0,e):
    z = input().split()
    n,N = int(z[0]),[int(_) for _ in z[1:]]
    abv = sum(N)/n
    N = [_ for _ in N if _ > abv]
    print("{:.3f}".format(round((100*len(N)/n),3))+"%")
