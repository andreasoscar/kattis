
p = int(input())
readings = list()
for i in range(p):
    readings.append(list(map(int, input().split())))


def find_node(n):
    #even we increase q
    #odd we increase p
    right = list()
    while n != 1:
        if n % 2:
            right.append(True)
        else:
            right.append(False)
        n = n // 2

    p,q = 1,1
    #reverse since we want to go from top to bottom now
    for direction in reversed(right):
        if direction:
            p = p+q
        else:
            q = p+q
    return p,q

for reading in readings:
    k,n = reading
    p,q = find_node(n)
    print(str(k) + " " + str(p) + "/" + str(q))
    