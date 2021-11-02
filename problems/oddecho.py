k = int(input())
l = []
for i in range(k):
    l.append(input())
for i in range(len(l)):
    if i % 2 == 0:
        print(l[i])