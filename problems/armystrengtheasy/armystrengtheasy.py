#!/usr/bin/python3
# problem: armystrengtheasy, rating: 2.2
from collections import deque
n = int(input())
a1,a2 = deque(),deque()
for i in range(n):
    t,v = input(),input()
    a1 = deque(sorted([int(_) for _ in input().split()]))
    a2 = deque(sorted([int(_) for _ in input().split()]))
    while len(a1) and len(a2) > 0:
        if a1[0] > a2[0]:
            a2.popleft()
        elif a1[0] < a2[0]:
            a1.popleft()
        elif a1[0] == a2[0]:
            a2.popleft()
    if len(a1) > len(a2):
        print("Godzilla")
    else:
        print("MechaGodzilla")
