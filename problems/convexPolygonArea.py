def shoelace_formula(cords):
    total = 0
    for i in range(len(cords)-1):
        pair_one = cords[i]
        pair_two = cords[i+1]
        total += pair_one[0] * pair_two[1] - pair_one[1] * pair_two[0]
    return (1/2)*total


nbr = int(input())
list_of_cords = list()
for i in range(nbr):
    inp = input()
    splitted_input = inp.split(" ")
    nbr_cords = int(splitted_input[0])
    cords = [int(x) for x in splitted_input[1:]]
    coordinates = list()
    for index in range(0, len(cords)-1, 2):
        coordinates.append((cords[index], cords[index+1]))
    coordinates.append(coordinates[0])
    list_of_cords.append(coordinates)

for cords in list_of_cords:
    print(shoelace_formula(cords))