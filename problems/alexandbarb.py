n,l,h = [int(x) for x in input().split(" ")]
xor = 0
if int(n) == 0:
    print("Barb")
else:
    v = bin((n^l)^h)[2:]
    for i in v:
        xor = (xor + int(i))%2
    if xor == 0:
        print("Barb")
    else:
        print("Alex")
