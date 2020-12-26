n,k = [int(x) for x in input().split()]
if n == 0 and k == 0:
    print("Not a moose")
elif n == k:
    print("Even " + str(max(n,k)*2))
else:
    print("Odd " + str(max(n,k)*2))
