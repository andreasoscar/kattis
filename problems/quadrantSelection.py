points = []
for i in range(2):
    points.append(int(input()))

x = points[0]
y = points[1]

if x > 0:
    if y > 0:
        print("1")
    else:
        print("4")
elif x < 0:
    if y > 0:
        print("2")
    else:
        print("3")
