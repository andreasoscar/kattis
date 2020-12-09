n,m = int(input()),int(input())
d = m/n
layout = []
if n == 1:
    st = ""
    for i in range(m):
        st = st + "*"
    print(st)
else:
    while True:
        if m % n == 0:
            for i in range(n):
                layout.append(['*']*(m//n))
            break
        else:
            n = n - 1
            m = m - int(d)
            layout.append(['*']*int(d))
for j in layout:
    st = ""
    for i in j:
        st = st + i
    print(st)
