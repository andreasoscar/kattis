n = input()
indices = []
line = "no hiss"
for k in range(0,len(n)):
    if n[k] == 's':
        indices.append(k)
for i in range(1,len(indices)):
    if indices[i] == indices[i-1] + 1:
        line = "hiss"
print(line)
