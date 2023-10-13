l = input()
n,t = l.split()
n = int(n)
t = int(t)
q = list()
for i in range(n):
    q.append(int(input()))

q = sorted(q, reverse=True)
res = list()
for i in range(0,n,1):
    res.append(q[0]-t*i)
if res[len(res)-1] > 0:
    print("YES")
else:
    print("NO")
