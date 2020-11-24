k = int(input())
while k > 0:
    c = input();
    if(c == "P=NP"):
        print("skipped")
        k = k - 1
    else:
        c = [int(item) for item in c.split('+')]
        print(c[0] + c[1])
        k = k - 1
