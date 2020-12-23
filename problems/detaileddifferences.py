t = int(input())
for i in range(t):
    s1,s2 = input(),input()
    print(s1)
    print(s2)
    for j in range(len(s1)):
        if s1[j] == s2[j]:
            print('.',end='')
        else:
            print('*',end='')
    print()
