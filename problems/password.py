rep = int(input())
list = []
for k in range(rep):
    list.append(input().split(' '))
total = 0
index = 1
list.sort(key=lambda tup: tup[1], reverse=True)
for k in list:
    total += float(k[1]) * index
    index += 1
print(round(total,5))
