import sys
values = []
p = 0
for line in sys.stdin:
    inc = line.strip().rstrip().split(' ')
    inc.pop(0)
    for i in range(len(inc)):
        inc[i] = int(inc[i])
    values.append(inc)

for i in values:
    v_min = int(min(i))
    v_max = int(max(i))
    v_range = v_max - v_min
    p = p + 1
    print("Case " + str(p) + ": " + str(v_min) + " " + str(v_max) + " " + str(v_range))
