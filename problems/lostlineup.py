n = input()
friends = [int(y) for y in input().split()]
s = sorted(friends)
print(str(1) + " ",end='')
for i in s:
    print(str(friends.index(i)+2) + " ",end='')