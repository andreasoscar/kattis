s,t,n = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
time = 0
for i in range(0,len(d)-1):
    time = time + d[i]
    time = time + time%c[i] + b[i]
time = time + d[len(d)-1]
if time >= t:
    print("no")
else:
    print("yes")
