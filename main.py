from itertools import groupby

####Functions:
def find_index_max(dictionary):
    #finds the max value of a dictionary based on the value. If value repeats itself, it chooses the highest key (room with more beds)
    max_value_dict = [key for key, value in thisdict.items() if value == max(thisdict.values())]
    keys = list(thisdict.keys())
    values = list(thisdict.values())

    if len(max_value_dict) > 1:
        indices = [index for index, val in enumerate(values) if val == max(values)]
        index_max = keys[max(indices)] - 1
    else:
        index_max = max(range(len(values)), key=values.__getitem__)
        index_max = keys[index_max] - 1
    return index_max

def answer (data, text):
    #prompts the final message
    print("")
    data = [list(g) for k, g in groupby(data, key=len)]
    print(f"{text.capitalize()} distribution:")
    
    for element in data:
        print(f"{len(element)} rooms of {len(element[0])} {text.lower()}.")

####Prompt dialogue and variable declaration:
input_room = [0 for a in range(5)] #change the number to the amount of max. beds per room
for idx, val in enumerate(input_room):
    input_room[idx] = int(input(f"How many bedrooms with {idx+1} bed(s)? "))

girls = int(input(f"How many girls? "))
boys = int(input(f"How many boys? "))

rooms_1bed = [[0]*1 for count in range(input_room[0])] #if you changed the number in line 5, you need to add a new variable
rooms_2bed = [[0]*2 for count in range(input_room[1])]
rooms_3bed = [[0]*3 for count in range(input_room[2])]
rooms_4bed = [[0]*4 for count in range(input_room[3])]
rooms_5bed = [[0]*5 for count in range(input_room[4])]

rooms_listoflists = [rooms_1bed, rooms_2bed, rooms_3bed, rooms_4bed, rooms_5bed]

thisdict = {
  1 : len(rooms_1bed),
  2 : len(rooms_2bed),
  3 : len(rooms_3bed),
  4 : len(rooms_4bed),
  5 : len(rooms_5bed),
}

####Code:

if __name__ == '__main__':
    while girls > 0 or boys > 0:
        if girls > boys:
            index_max = find_index_max(thisdict)
            #First looks for the type of room most availabel
            for idx, val in enumerate(rooms_listoflists[index_max]):
                if girls > 0 and all(item == 0 for item in val):
                    #Then loops through it and looks for empty spaces
                    for element in range(len(rooms_listoflists[index_max])):
                        if all(item == 0 for item in rooms_listoflists[index_max][element]):
                            #If empty spaces are found, they're taken
                            rooms_listoflists[index_max][element] = [1 for i in range(0,len(rooms_listoflists[index_max][element]))]
                            #Substracts the number of spaces distributed for the girls
                            girls = girls - len(rooms_listoflists[index_max][element])
                            #The number of availables beds is reduced in the dictionary
                            thisdict[index_max+1] = thisdict[index_max+1] - 1
                            break
                    #We have to break in order to test again that girls still bigger than 0
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

    answer(girls_rooms, "girls")
    answer(boys_rooms, "boys")
