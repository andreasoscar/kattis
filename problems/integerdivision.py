n,d = [int(y) for y in input().split()]
a = [int(y)//d for y in input().split()]
z = dict(zip(a,[0]*len(a)))
nbr = 0
for i in a:
    z[i] += 1
for k in z.values():
    #for 5 4, 4 5 6 7 8, [1,1,1,1,2], 1st 1 with the 1s after, 1+1+1,
    #2nd 1, with 1s after, 1+1
    #3rd 1, with 1s after, 1
    #total = 1+1+1 + 1+1 + 1 = 6, we have k*(k-1)/2 possible combinations
    nbr += k*(k-1)*1/2
print(int(nbr))
