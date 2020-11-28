n,h,v = [int(p) for p in input().split()]
s1,s2,s3,s4 = v*h*4,(n-v)*h*4,(n-h)*v*4,(n-h)*(n-v)*4
print(max(s1,s2,s3,s4))
