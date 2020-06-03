k = int(input())

cases = []

for i in range(k):
    cases.append(input().split(' '))

for k in cases:

    #i[0], expected revenue if not advertising
    #[1], expected revenue if advertising
    #i[2], cost of advertising
    diff = int(k[1]) - int(k[0]) - int(k[2])
    if int(k[1]) > int(k[0]) and diff > 0:
        print("advertise")
    elif diff == 0:
        print("does not matter")
    else:
        print("do not advertise")
