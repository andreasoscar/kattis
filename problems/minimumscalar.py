nbr = int(input())
cases = []
v = 0
while nbr > 0:
    sum1 = 0
    k = int(input())
    if(len(str(k)) == 1):
        sum1 = 0
    v1 = input().split()
    v2 = input().split()
    v1 = [int(item) for item in v1]
    v2 = [int(item) for item in v2]
    v1.sort()
    v2.sort()
    for i in range(0,k):
        sum1 += int(v1[i])*int(v2[k-i-1])
    v+= 1
    cases.append("Case #" + str(v) + ": " + str(sum1))
    nbr = nbr - 1
for i in cases:
    print(i)
