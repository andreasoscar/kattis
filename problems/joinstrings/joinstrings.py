#!/usr/bin/python3
# problem: joinstrings, rating: 5.1
n = int(input())
s = dict()
for i in range(n):
    s[i] = input()
for i in range(n-1):
    a,b = [int(x) for x in input().split()]
    s[a-1] = s[a-1] + s[b-1]
    s[b-1] = ""
    s.pop(b-1,None)
j = list(s.keys())
print(s[j[0]])
