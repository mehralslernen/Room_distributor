from itertools import groupby

input_room = [0 for a in range(5)]
for idx, val in enumerate(input_room):
    input_room[idx] = int(input(f"How many bedrooms with {idx+1} bed(s)? "))

girls = int(input(f"How many girls? "))
boys = int(input(f"How many boys? "))

rooms_1bed = [[0]*1 for count in range(input_room[0])]
rooms_2bed = [[0]*2 for count in range(input_room[1])]
rooms_3bed = [[0]*3 for count in range(input_room[2])]
rooms_4bed = [[0]*4 for count in range(input_room[3])]
rooms_5bed = [[0]*5 for count in range(input_room[4])]

rooms_available = [len(rooms_1bed), len(rooms_2bed), len(rooms_3bed), len(rooms_4bed), len(rooms_5bed)]
rooms_listoflists = [rooms_1bed, rooms_2bed, rooms_3bed, rooms_4bed, rooms_5bed]

thisdict = {
  1 : len(rooms_1bed),
  2 : len(rooms_2bed),
  3 : len(rooms_3bed),
  4 : len(rooms_4bed),
  5 : len(rooms_5bed),
}


def find_index_max(dictionary):
    max_value_dict = [key for key, value in thisdict.items() if value == max(thisdict.values())]

    if len(max_value_dict) > 1:
        keys = list(thisdict.keys())
        values = list(thisdict.values())

        maxval = max(values)
        indices = [index for index, val in enumerate(values) if val == maxval]
        index_max = keys[max(indices)] - 1
    else:
        keys = list(thisdict.keys())
        values = list(thisdict.values())
        index_max = max(range(len(values)), key=values.__getitem__)
        index_max = keys[index_max]-1

    return index_max

while girls > 0 or boys > 0:
    if girls > boys:

        index_max = find_index_max(thisdict)
        for idx, val in enumerate(rooms_listoflists[index_max]):
            if girls > 0 and all(item == 0 for item in val):
                for element in range(len(rooms_listoflists[index_max])):
                    if all(item == 0 for item in rooms_listoflists[index_max][element]):
                        rooms_listoflists[index_max][element] = [1 for i in range(0,len(rooms_listoflists[index_max][element]))]
                        girls = girls - len(rooms_listoflists[index_max][element])

                        thisdict[index_max+1] = thisdict[index_max+1] - 1
                        break
                break
            else:
                pass
        
    else:
        index_max = find_index_max(thisdict)
        for idx, val in enumerate(rooms_listoflists[index_max]):
            if boys > 0 and all(item == 0 for item in val):
                for element in range(len(rooms_listoflists[index_max])):
                    if all(item == 0 for item in rooms_listoflists[index_max][element]):
                        rooms_listoflists[index_max][element] = [2 for i in range(0,len(rooms_listoflists[index_max][element]))]
                        boys = boys - len(rooms_listoflists[index_max][element])

                        thisdict[index_max+1] = thisdict[index_max+1] - 1
                        break
                break
            else:
                pass
        
girls_rooms = []
boys_rooms = []

for rooms in rooms_listoflists:
    for element in rooms:
        if all(item != 0 for item in element) and all(item == 1 for item in element):
            girls_rooms.append(element)
        elif all(item != 0 for item in element) and all(item == 2 for item in element):
            boys_rooms.append(element)
        else:
            pass

girls_rooms = [list(g) for k, g in groupby(girls_rooms, key=len)]
boys_rooms = [list(g) for k, g in groupby(boys_rooms, key=len)]

print("Girls distribution:")
for element in girls_rooms:
    print(f"{len(element)} rooms of {len(element[0])} girls.")

print("Boys distribution:")
for element in boys_rooms:
    print(f"{len(element)} rooms of {len(element[0])} boys.")