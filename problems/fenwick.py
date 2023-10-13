import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl_2(): return list(inp().split())
def nl(): return [int(tok) for tok in inp().split()]

n,q = nl()

A = [0]*n

def prefix_sum(i):
    sum_ = 0
    i = i - 1
    while i >= 0:
        sum_ += A[i]
        i = (i & (i+1)) - 1
    return sum_

def add(i, delta):
    while i < n:
        A[i] += delta
        i = i | (i+1)

for c in range(q):
    operator, *rest = nl_2()
    if operator == "+":
        l,r = map(int, rest)
        add(l,r)
    elif operator == "?":
        i = int(*rest)
        print(prefix_sum(i))
    
