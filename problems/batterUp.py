k = int(input())
list1 = list(map(int, input().split(' ')))
for x in list1:
    if x == -1:
        k = k - 1
list1 = list(filter(lambda x: int(x) >= 0, list1))
print(sum(list1)/int(k))
