T = int(input())
eq = []
for q in range(T):
    a1,n1,b1,m1 = [int(x) for x in input().split()]
    eq.append([(a1,n1),(b1,m1)])
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
def remainder(a):
    a0,a1 = a[0],a[1]
    N = 1
    g =  gcd(a0[1],a1[1])
    if a0[0] % g != a1[0] % g:
        return "no solution"
    else:
        z = a0[1] / g*a1[1]
        p,q = euclides_extended_algorithm(a0[1]/g,a1[1]/g)
        y = (a0[0]*(a1[1]*g)*q + a1[0]*(a0[1]/g)*p) % z
        return y%z,z
for i in eq:
    rem = remainder(i)
    if len(rem) > 2:
        print(rem)
    else:
        print(str(int(rem[0])) + " " + str(int(rem[1])))
