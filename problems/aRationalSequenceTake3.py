n_lines = int(input())

def calc(n):
    iterated = 0
    p,q = 1,1


def calcLeaf(p,q,n):
    while n > 0:
        if p >= q:
            q = p+q
            n = n - 1
        else:
            p = p+q
            n = n - 1
        



    
    


        

for i in range(n_lines):
    k,n = [int(inp) for inp in input().split()]
    calc(n)
    #print(str(k) + " " + str(calc(n)) + "\n")
    
    