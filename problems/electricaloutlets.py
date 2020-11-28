n = int(input())
for i in range(0,n):
    t = [int(x) for x in input().split()][1:]
    print(sum(t)-len(t)+1)
