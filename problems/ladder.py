import math
parameters = input().split(' ')

h = parameters[0]
v = parameters[1]
radians = float(v) * math.pi / 180
l =  float(h)/(abs(math.sin((radians))))

print(math.ceil(l))
