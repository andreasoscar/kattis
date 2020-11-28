a,k,q,j,t,t9,t8,t7 = [11,11],[4,4],[3,3],[20,2],[10,10],[14,0],[0,0],[0,0]
n,b = input().split()
sum = 0
for i in range(0,4*int(n)):
    z = input()
    if z[0] == 'A':
        sum = sum + 11
    elif z[0] == 'K':
        sum = sum + 4
    elif z[0] == 'Q':
        sum = sum + 3
    elif z[0] == 'T':
        sum = sum + 10
    elif z[0] == 'J':
        if z[1] == b:
            sum = sum + 20
        else:
            sum = sum + 2
    elif z[0] == '9':
        if z[1] == b:
            sum = sum + 14
print(sum)
