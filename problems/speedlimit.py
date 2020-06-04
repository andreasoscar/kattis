values = []
carry = 0
while True:
    nbr = 0
    k = input().split()
    if k[0] == "-1":
        break
    else:
        total = 0
        if len(k) == 1:
            nbr = int(k[0])
            carry = 0
        for c in range(nbr):
            inputs = input().split()
            total += int(inputs[0]) * (int(inputs[1]) - carry)
            carry = int(inputs[1])
        values.append(total)
for v in values:
    print(str(v) + " miles")
