dict = {}
import sys
queries = []
query = False
for line in sys.stdin:
    if query:
        queries.append(line.rstrip())
    elif not query and not line == "\n":
        d,m = [i for i in line.rstrip().split()]
        dict[d] = m
    if line == "\n":
        query = True
inv_map = {v: k for k, v in dict.items()}
for i in queries:
    if i in inv_map.keys():
        print(inv_map[i], end='\n')
    else:
        print("eh",end='\n')
