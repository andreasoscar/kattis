k = str(input())


while(True):
    t = 1;
    for i in k:
        if(int(i) != 0):
            t = t*int(i)
    k = str(t)
    if(len(str(k)) == 1):
        break
print(k)
