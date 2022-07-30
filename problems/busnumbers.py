import math
n = int(input())
newRanges = []

values = [int(i) for i in input().split(" ")]
tf = [False] * (max(values)+1)
values.sort()

for i in values:
    tf[i] = True
    
for i in values:
    t = i
    startRange = i 
    endRange = i
    if tf[t]:
        while(t+1 < len(tf) and tf[t+1]):
            t += 1
            endRange = t
        if(startRange != endRange and startRange+1 != endRange):
            newRanges.append(str(startRange) + "-" + str(endRange))
            for i in range(startRange+1, endRange+1):
                tf[i] = False
        else:
            if not tf[i-1]:
                newRanges.append(startRange)
                if(startRange+1==endRange):
                    newRanges.append(endRange)
for i in newRanges:
    print(i, end=' ')

    
        
    

