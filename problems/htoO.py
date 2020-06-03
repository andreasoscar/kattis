import re
available = input()
desired = input()
elements = {}
#factor = int(available[1])
#print(factor)
totalAvailable = 0
savedVar = ""
#print(available)
lastWasInt = False
storedValue = 0
#available.remove(' ')
# for k in list(available[0]):
#     if not k.isnumeric() and elements.get(k) == None:
#         savedVar = k
#         elements.update({k : 1})
#     elif not elements.get(k) == None:
#         savedVar = k
#         elements.update({k : elements.get(k)+1})
#     elif k.isnumeric() and lastWasInt:
#         print(str(storedvalue) + str(k))
#         #print(concat)
#         #elements.update({savedVar : concat})
#     elif k.isnumeric():
#         storedvalue = lastWasInt
#         lastWasInt = True
#         elements.update({savedVar : int(k)})
#
# for k in elements:
#     elements.update({ k : elements.get(k)*factor})
# print(elements)

# chems = {}
# print(list(desired))
# for k in list(desired):
#     if not k.isnumeric() and chems.get(k) == None:
#         savedVar = k
#         chems.update({k : 1})
#     elif not chems.get(k) == None:
#         savedVar = k
#         chems.update({k : chems.get(k)+1})
#     elif k.isnumeric():
#         chems.update({savedVar : int(k)})
#
# print(chems)
