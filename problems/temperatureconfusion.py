from fractions import Fraction
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
f = input()
c = 5*(Fraction(f)-32)/9
n,d = Fraction(c).numerator, Fraction(c).denominator
g = gcd(n,d)
n,d = n/g, d/g
print(str(int(n)) + "/" + str(int(d)))
