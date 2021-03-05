from functools import reduce
print(reduce(lambda x, y: x*y, [int(_) for _ in input().split()]))
