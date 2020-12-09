def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
def euclides_extended_algorithm(z,n):
    if z == 0:
        return 0,1
    z1,n1 = euclides_extended_algorithm(n%z,z)
    t1 = n1 - (n//z) * z1
    t2 = z1
    return t1,t2

while True:
    n,t = [int(i) for i in input().split(" ")]
    if n == 0 and t == 0:
        break
    else:
        for i in range(0,t):
            x,y,z = [i for i in input().split(" ")]
            x,z = int(x),int(z)
            if y == "/":
                if gcd(z,n) == 1:
                    print((x * euclides_extended_algorithm(z,n)[0])%n)
                else:
                    print("-1")
            elif y == "*":
                print((x*z)%n)
            elif y == "+":
                print((x+z)%n)
            elif y == "-":
                print((x-z)%n)
