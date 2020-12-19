n,p = [int(_) for _ in input().split()]
problems = [int(_) for _ in input().split()]
first = problems[p]
del problems[p]
problems.sort()
if first > 300:
    print(0,0)
else:
    penalty,solved = first,1
    left = 300-penalty
    for i in problems:
        left -= i
        if left < 0:
            break
        solved += 1
        penalty += 300-left
    print(solved,penalty)
