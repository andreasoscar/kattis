x = [int(t) for t in input().split(" ")]
combi = ["+","-","/","*","="]
valid = []
for i in combi:
    for j in combi:
        if j != "=" and i == "=":
            if eval(str(x[0]) + j + str(x[1])) == int(x[2]):
                valid.append(str(x[0]) + j + str(x[1]) + i + str(x[2]))
        elif j == "=" and i != "=":
            if int(x[0]) ==  eval(str(x[1]) + i + str(x[2])):
                valid.append(str(x[0]) + j + str(x[1]) + i + str(x[2]))
if len(valid) > 0:
    print(valid[0])
