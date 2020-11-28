a,b,c = 1,2,3
ballPos = 1
n = input()
for i in n:
    if i == "A" and ballPos == 1:
        ballPos = 2
    elif i == "A" and ballPos == 2:
        ballPos = 1
    elif i == "B" and ballPos == 1:
        ballPos == 1
    elif i == "B" and ballPos == 2:
        ballPos = 3
    elif i == "B" and ballPos == 3:
        ballPos = 2
    elif i == "C" and ballPos == 1:
        ballPos = 3
    elif i == "C" and ballPos == 2:
        ballPos = 2
    elif i == "C" and ballPos == 3:
        ballPos = 1

print(ballPos)
