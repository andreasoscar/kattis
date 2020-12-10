votes = dict()
while True:
    z = input()
    if z == "***":
        break
    else:
        if z in votes.keys():
            votes[z] = votes[z]+1
        else:
            votes[z] = 1
v = int(votes[max(votes,key=votes.get)])
if len([i for i in votes.values() if i == v]) > 1:
    print("Runoff!")
else:
    print(max(votes,key=votes.get))
