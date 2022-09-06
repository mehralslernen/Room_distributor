
'''

Input: arrays with different lengths (for rooms) and 2 variables with numbers (girls and boys)

arr0 = NA
arr1
arr2
...

girls = x
boys = y

arr_lengths = [len(arr0), len(arr1), ...]
arr_listoflists = [arr0, arr1, ...]

While (g and b unequal or bigger than 0) -> loop:
	If g > b:
		idx = idx from max(arr_lengths)
		for val in arr_listoflists[idx]:
			if g unequal or bigger than 0:
				val = g
				g = g-1
			else:
				pass
		arr_lengths = arr_lengths.pop(arr_lengths[idx])
		arr_listoflists = arr_listoflists.pop(arr_listoflists[idx])		
	Elif g = b:
		same as above
	Else:
		same as above

arr_listoflists = [arr0, arr1, ...]

for array in arr_listoflists :
	if array != completely(NA):
		dict.append(arr: [g/b, len(arr)]

print(girls)
for y in dict where dict(g):
	room with y beds

print(boys)
for y in dict where dict(b):
	room with y beds

'''





input_room = [0,2,1,2,3]

rooms_1bed = [[0]*1 for count in range(input_room[0])]
rooms_2bed = [[0]*2 for count in range(input_room[1])]
rooms_3bed = [[0]*3 for count in range(input_room[2])]
rooms_4bed = [[0]*4 for count in range(input_room[3])]
rooms_5bed = [[0]*5 for count in range(input_room[4])]

rooms_available = [len(rooms_1bed), len(rooms_2bed), len(rooms_3bed), len(rooms_4bed), len(rooms_5bed)]

thisdict = {
  1 : len(rooms_1bed),
  2 : len(rooms_2bed),
  3 : len(rooms_3bed),
  4 : len(rooms_4bed),
  5 : len(rooms_5bed),
}

print(thisdict)

rooms_listoflists = [rooms_1bed, rooms_2bed, rooms_3bed, rooms_4bed, rooms_5bed]

girls = 18
boys = 10

while girls > 0 or boys > 0:
    if girls > boys:
        #print("Begin girls", girls, rooms_listoflists)

        index_max = int(max(range(len(rooms_available)), key=rooms_available.__getitem__))


        for idx, val in enumerate(rooms_listoflists[index_max]):
            if girls > 0 and all(item == 0 for item in val):
                for element in range(len(rooms_listoflists[index_max])):
                    if all(item == 0 for item in rooms_listoflists[index_max][element]):
                        rooms_listoflists[index_max][element] = [1 for i in range(0,len(rooms_listoflists[index_max][element]))]
                        girls = girls - len(rooms_listoflists[index_max][element])

                        print(rooms_available)
                        print(index_max)

                        max_keys = [key for key, value in thisdict.items() if value == max(thisdict.values())]
                        print(max_keys)

                        if 


                        rooms_available[index_max] = rooms_available[index_max] - 1
                        break
                break
            else:
                pass
        
        #del rooms_listoflists[index_max]

        #print("End girls", girls, rooms_listoflists)
    elif girls == 1:
        #print(boys, girls)
        break

    else:
        #print("Begin boys", boys, rooms_listoflists)

        index_max = int(max(range(len(rooms_available)), key=rooms_available.__getitem__))

        for idx, val in enumerate(rooms_listoflists[index_max]):
            if boys > 0 and all(item == 0 for item in val):
                for element in range(len(rooms_listoflists[index_max])):
                    if all(item == 0 for item in rooms_listoflists[index_max][element]):
                        rooms_listoflists[index_max][element] = [2 for i in range(0,len(rooms_listoflists[index_max][element]))]
                        boys = boys - len(rooms_listoflists[index_max][element])
                        rooms_available[index_max] = rooms_available[index_max] - 1
                        break
                    else:
                        pass
                break
            else:
                pass
            
        #print("End boys", boys, rooms_listoflists)

#print(rooms_listoflists)


'''
If g > b:
		idx = idx from max(arr_lengths)
		for val in arr_listoflists[idx]:
			if g unequal or bigger than 0:
				val = g
				g = g-1
			else:
				pass
		arr_lengths = arr_lengths.pop(arr_lengths[idx])
		arr_listoflists = arr_listoflists.pop(arr_listoflists[idx])	


'''


















'''
Prompt dialogues:

input_room = [0 for a in range(5)]
for idx, val in enumerate(input_room):
    input_room[idx] = int(input(f"How many bedrooms with {idx+1} bed(s)? "))

girls = int(input(f"How many girls? "))
boys = int(input(f"How many boys? "))


'''
