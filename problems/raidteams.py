nbrPlayers = int(input())
players = []
teams = []
team = []
count = 1
pick = 0

def kq(v):
    nbr = ""
    for c in v:
        if c.isdigit():
            nbr = nbr + c
    return int(nbr)
for k in range(nbrPlayers):
    players.append(input().split())
for k in range(nbrPlayers):
    if count == 3:
        if pick == 3:
            count = 1
            pick = 0
    if pick == 3:
        count += 1
        pick = 0
    pick += 1
    best = max(players,key=lambda x:x[count])
    candidates = []
    candidates.append(best)
    for q in players:
        if not q == best:
            if q[count] == best[count]:
                candidates.append(q)
    candidates.sort(key=lambda x: kq(x[0]))
    if len(candidates) > 0:
        if not best == candidates[0]:
            best = candidates[0]
        players.remove(best)
    if len(team) < 3:
        team.append(best)
    if len(team) == 3:
        teams.append(team)
        team = []
for v in teams:
    v.sort(key=lambda x:kq(x[0]))
    y = ""
    for q in v:
        y = y + q[0] + " "
    print(y)
