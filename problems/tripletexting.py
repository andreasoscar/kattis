s = input()
k = int(len(s)/3)
if s[0:k] == s[k:(2*k)]:
    print(s[0:k])
elif s[k:(2*k)] == s[(2*k):(3*k)]:
    print(s[k:2*k])
elif s[(2*k):(3*k)] == s[0:k]:
    print(s[(2*k):(3*k)])
