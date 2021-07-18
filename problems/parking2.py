n = int(input())
for i in range(n):
    stores = int(input())
    storeList = [int(i) for i in input().split()]
    best = sum(storeList)/stores
    print(int((best-min(storeList))*2 + (max(storeList)-best)*2))
