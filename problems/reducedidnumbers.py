nbr = int(input())
values = []
tries = []
incr = 1
for i in range(nbr):
    values.append(int(input()))
tries = [0]*(len(values))
while True:
    for i in range(len(values)):
        v = values[i] % incr
        if tries[i] == 0:
            tries[i] = v
    if len(tries) == len(set(tries)):
        print(incr)
        break
    else:
        incr += 1
        tries = [0]*len(values)
