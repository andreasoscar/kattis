n = int(input())
for i in range(n):
    nbrPersons = int(input())
    if nbrPersons == 1:
        lengths = [int(_) for _ in input().split(' ')[1:]]
        print("{:.8f}".format(sum(lengths)));
    else:
        length = []
        waitingTime = []
        previous = 0
        for i in range(nbrPersons):
            values = [int(_) for _ in input().split(' ')[1:]]
            length.append(sum(values))
        length.sort()
        for i in length:
            waitingTime.append(i + previous)
            previous = i + previous
        print("{:.8f}".format(sum(waitingTime)/nbrPersons));
