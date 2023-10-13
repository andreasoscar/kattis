k = int(input())
inputs = []
for i in range(k):
	inputs.append(int(input()))

fibnumbers = [1,1]

def fib(n,i):
	for i in range(2,n):
		fibnumbers.append((fibnumbers[i-1]%i+fibnumbers[i-2]%i))


for i in inputs:
	fib(50,i)
	fibvec = {}
	ite = 1
	for q in fibnumbers[2:]:
		if not q in fibvec.keys():
			fibvec[q] = 1
		else:
			print(ite)
			break
		ite += 1


