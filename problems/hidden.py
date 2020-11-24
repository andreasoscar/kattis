M, I = input().split()
M = [char for char in M]
i = 0
while True:
    if(len(M) == 0):
        print("PASS")
        break
    elif(i >= len(I)):
        print("FAIL")
        break
    elif(I[i] in M and not M[0] == I[i]):
        print("FAIL")
        break
    elif(I[i] == M[0]):
        M.pop(0)
        i+=1
    else:
        i+=1
