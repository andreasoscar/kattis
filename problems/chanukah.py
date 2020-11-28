t = int(input())
vals = []
for i in range(0,t):
    vals.append(int((input().split())[1]))
for i in range(0,len(vals)):
    print(str(i+1) + " " + str(int((1/2 * vals[i]*(1+vals[i]))) + vals[i]))
