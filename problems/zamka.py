L = int(input())
D = int(input())
X = int(input())
N = L
sub_n = []
def sum_d(n):
    s = 0
    for i in str(n):
        s = s + int(i)
    return s
while L <= N and N <= D:
    if sum_d(N) == X:
        sub_n.append(N)
        N = N + 1
    else:
        N = N + 1
print(min(sub_n))
print(max(sub_n))
