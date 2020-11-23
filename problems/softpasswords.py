S,P = input(),input()
T = False
if(S == P):
    T = True
elif(S == P.swapcase()):
    T = True
for i in [0,len(S)-1]:
    if(S[i].isdigit() and (S[i] + P == S or P + S[i] == S)):
        T = True
if(not T):
    print("No")
else:
    print("Yes")
