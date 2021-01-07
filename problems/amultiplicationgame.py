import sys
data = []
for i in sys.stdin:
    data.append(int(i))
for t in data:
    l,h = 1,9
    turn = 1
    if t <= 9:
        print("Stan wins.")
    while not l <= t <= h:
        turn += 1
        if turn % 2 == 0:
            l = h + 1
            h = h * 2
        elif turn % 2 != 0:
            l = h + 1
            h = h * 9
    if turn % 2 == 0:
        print("Ollie wins.")
    else:
        print("Stan wins.")
