while True:
    k = input()
    if k == "0 0":
        break
    else:
        i,j = [int(x) for x in k.split()]
        print(str(int(i/j)) + " " + str(i%j) + " / " + str(j))
