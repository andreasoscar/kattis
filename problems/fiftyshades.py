n = int(input())
i = 0
for j in range(n):
    z = input()
    if "pink" in z.lower() or "rose" in z.lower():
        i += 1
if i > 0:
    print(i)
else:
    print("I must watch Star Wars with my daughter")
