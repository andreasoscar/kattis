import sys
defs = {}
for line in sys.stdin:
    inp = line.strip('\n').split(' ')
    if inp[0] == "clear":
        defs = {}
    elif inp[0] == "def":
        defs[inp[1]] = int(inp[2])
    else:
        value = 0
        f = False
        for i in range(1,len(inp)):
            if inp[i] in defs.keys():
                if i == 1:
                    value += defs[inp[i]]
                if i > 1 and inp[i-1] == '-':
                    value = value - defs[inp[i]]
                elif i > 1 and inp[i-1] == '+':
                    value = value + defs[inp[i]]
            else:
                if inp[i] != '+' and inp[i] != '-' and inp[i] != '=':
                    f = True
                    break
        if f:
            finals = ""
            for s in range(1,len(inp)-1):
                finals += (inp[s] + ' ')
            finals += inp[len(inp)-1]
            print(finals + ' unknown')
        else:
            finals = ""
            z = False
            for s in range(1,len(inp)-1):
                finals += (inp[s] + ' ')
            finals += inp[len(inp)-1]
            for k,v in defs.items():
                if v == value:
                    z = True
                    break
            if z:
                print(finals + ' ' + k)
            else:
                print(finals + ' unknown')
