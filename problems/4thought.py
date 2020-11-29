k = int(input())
v = []
for i in range(0,k):
    v.append(int(input()))
p = ["*","+","-","//"]
ans = ["no solution" for b in range(0,len(v))]
for q in p:
    for t in p:
        for z in p:
            h = "4 " + z  + " 4 " + t + " 4 " +  q + " 4"
            if eval(h) in v:
                if ans[v.index(eval(h))] == "no solution":
                    ans[v.index(eval(h))] = h.replace("//","/") + " = " + str(int(eval(h)))
for w in ans:
    print(w)
