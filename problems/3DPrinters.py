import math
k = int(input())


#DEPRECATED SOLUTION, ONLY WORKS IN 6/33 CASES
def r1(n):
    return math.ceil(n * 1) / 1
# daysPrintingPrinters = (math.log10(k)*3)
# totalPrinters = math.pow(2, daysPrintingPrinters)
# totalDays = k/(totalPrinters) + daysPrintingPrinters
# print(int(r1(totalDays)))

i = 0
while(i + k/math.pow(2,i) > i+1 + k/math.pow(2,i+1)):
    i += 1
    #while loop done, lets check value for i
print(int(r1(i + k/math.pow(2,i))))
