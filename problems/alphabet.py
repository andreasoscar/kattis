s = input()
nbr = 0
f = False
so = ''.join(sorted(s))
for k in range(len(so)):
    if s[k:] + s[:k] == so:
        f = True
        break
    elif ord(so[k]) < ord(s[k]):
        nbr += 1
if f:
    print(nbr)
else:
    print(26-nbr)
