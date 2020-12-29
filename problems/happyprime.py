k = int(input())
candidates = []
ishappy = ["YES"]*(k)
def happy(k):
    tried = set()
    while k > 1 and not k in tried:
        tried.add(k)
        k = sum(int(x)**2 for x in str(k))
    if k in tried:
        return False
    else:
        return True
for j in range(k):
    candidates.append(int(input().split()[1]))
for j in range(len(candidates)):
    hold = candidates[j]
    if hold > 1:
        for k in range(2,hold):
            if hold % k == 0:
                ishappy[j] = "NO"
                break
    else:
        ishappy[j] = "NO"
    if ishappy[j]:
        if not happy(hold):
            ishappy[j] = "NO"
i = 1
for k in range(len(ishappy)):
    print(str(i) + " " + str(candidates[k]) + " " + ishappy[k])
    i += 1
