T = int(input())
eq = []
for q in range(T):
    a1,n1,b1,m1 = [int(x) for x in input().split()]
    eq.append([(a1,n1),(b1,m1)])
def euclides_extended_algorithm(z,n):
    if z == 0:
        return 0,1
    z1,n1 = euclides_extended_algorithm(n%z,z)
    t1 = n1 - (n//z) * z1
    t2 = z1
    return t1,t2
def remainder(a):
    N = 1
    ai,yi,zi,m = [],[],[],[]
    for i in a:
        N = N * i[1]
        ai.append(i[0])
        m.append(i[1])
    for i in a:
        yi.append(N//i[1])
    for i in range(len(m)):
        inverse = euclides_extended_algorithm(yi[i],m[i])[0]
        zi.append(inverse%m[i])
    sum = 0
    for z in range(len(zi)):
        sum += ai[z]*yi[z]*zi[z]
    return sum%N,N
for i in eq:
    rem = remainder(i)
    print(str(rem[0]) + " " + str(rem[1]))
