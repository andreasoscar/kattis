import math
line1 = input()
line2 = input()

values1 = line1.split(' ')
values2 = line2.split(' ')
mSegment = float(values1[0])
nRings = float(values1[1])
radius = float(values1[2])

point1 = tuple((int(values2[0]), int(values2[1])))
point2 = tuple((int(values2[2]), int(values2[3])))

def getAngle(n,k):
    thetaAbs = abs(n-k)
    return 180*thetaAbs/mSegment

theta = getAngle(point1[0],point2[0])
distOrigo = 0
def getTotal():
    if point1[1] == point2[1]:
        distOrigo = point1[1]*radius/nRings
        if distOrigo*2 < (theta/360)*math.pi*2*distOrigo:
            return distOrigo * 2
        else:
            return (theta/360)*math.pi*2*distOrigo
    else:
        distOrigo = min(point1[1], point2[1])*radius/nRings
        if point1[1] == 0 or point2[1] == 0:
            if distOrigo * 2 > ((theta/360)*math.pi*2*distOrigo):
                return abs(point1[1]-point2[1])*radius/nRings + ((theta/360)*math.pi*2*distOrigo)
            else:
                return distOrigo*2 +  abs(point1[1]-point2[1])*radius/nRings
        elif point1[0] == 0 or point2[0] == 0:
            if distOrigo * 2 > ((theta/360)*math.pi*2*distOrigo):
                return abs(point1[1]-point2[1])*radius/nRings + ((theta/360)*math.pi*2*distOrigo)
            else:
                return distOrigo*2 + abs(point1[1]-point2[1])*radius/nRings
        elif distOrigo * 2 > ((theta/360)*math.pi*2*distOrigo):
            return ((theta/360)*math.pi*2*distOrigo + abs(point1[1]-point2[1])*radius/nRings)
        else:
            return distOrigo*2 + abs(point1[1]-point2[1])*radius/nRings

totalDistance = getTotal()
print(str(round(totalDistance, 18)))
