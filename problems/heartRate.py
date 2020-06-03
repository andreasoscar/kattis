k = int(input())
inputs = []
for i in range(k):
    inputs.append(input().split(' '))

for v in inputs:
    print(str(60*(float(v[0])-1)/float(v[1])) + " " + str(60*float(v[0])/float(v[1])) + " " + str(60*(float(v[0])+1)/float(v[1])))
