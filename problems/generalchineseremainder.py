T = int(input())
ai,ni = [],[]
for q in range(T):
    a1,n1,a2,n2 = [int(x) for x in input().split()]
    ai.append([a1,a2])
    ni.append([n1,n2])
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
def euclides_extended_algorithm(z,n):
    if z == 0:
        return 0,1
    z1,n1 = euclides_extended_algorithm(n%z,z)
    t1 = n1 - (n//z) * z1
    t2 = z1
    return t1,t2
def remainder(a,n):
    a1,a2,n1,n2 = a[0],a[1],n[0],n[1]
    g = gcd(n1,n2)
    #print(g)
    if a1%g != a2%g:
        print("no solution")
    else:
        u,v= euclides_extended_algorithm(n1//g,n2//g)
        w = n1//g * n2
        x = (a1*(n2//g)*v + a2*(n1//g)*u)%w
        print(x%w,w)
for i in range(len(ai)):
    remainder(ai[i],ni[i])
