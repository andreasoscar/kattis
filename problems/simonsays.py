N = int(input())
L = []
for k in range(N):
    inc = input()
    if inc[0:10] == "Simon says":
        print(inc[11:])
