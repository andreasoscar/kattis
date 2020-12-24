n = int(input())
def sum(y):
    sum = 0
    for i in y:
        sum += int(i)
    return sum
while n % sum(str(n)) != 0:
    n += 1
print(n)
