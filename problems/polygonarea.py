points = []
while True:
    k = input().split()
    if len(k) == 1 and not k[0] == "0":
        sum = 0
        rotation = "CW"
        for i in range(int(k[0])):
            points.append(input().split())
        for y in range(len(points)-1):
            sum += int(points[y][0]) * int(points[y+1][1]) - int(points[y][1]) * int(points[y+1][0])
        sum += int(points[len(points)-1][0]) * int(points[0][1]) - int(points[len(points)-1][1]) * int(points[0][0])
        if sum > 0:
            rotation = "CCW"
        points = []
        print(rotation + " " + str(abs(sum/2)))
    else:
        break
