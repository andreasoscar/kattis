nbr = int(input())
citations = []
for i in range(nbr):
    citations.append(int(input()))
counts = [0]*len(citations)
citations.sort()
copy = citations.copy()
for i in range(len(citations)):
        counts[i] = len(citations)
        citations.pop()
maxValue = 0
for i in range(len(counts)):
    if counts[i] >= copy[i] and copy[i] > maxValue:
        maxValue = copy[i]
    elif copy[i] >= counts[i] and counts[i] > maxValue:
        maxValue = counts[i]
print(maxValue)
