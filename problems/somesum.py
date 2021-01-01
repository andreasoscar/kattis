N = int(input())
i,v = 0,0
for j in range(100-N+1,101):
    i += j
for j in range(1,1+N):
    v += j
if i % 2 == 0 and v % 2 != 0 or i % 2 != 0 and v % 2 == 0:
    print("Either")
elif i % 2 == 0 and v % 2 == 0:
    print("Even")
elif i % 2 != 0 and v % 2 != 0:
    print("Odd")
