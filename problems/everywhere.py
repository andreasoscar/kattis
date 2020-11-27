h = []
k = int(input())
for i in range(0,k):
    cities = []
    m = int(input())
    while m > 0:
        z = input()
        if not z in cities:
            cities.append(z)
        m = m - 1
    h.append(len(cities))
for x in h:
    print(x)
