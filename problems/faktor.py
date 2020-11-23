from functools import reduce
print(reduce(lambda x,y: (int(x)*int(y))-(int(x)-1), input().split()))
