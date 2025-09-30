paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]
dates = [1939, 1933, 1946, 1940]

#Combine the paintings and dates lists into a list of tuples (painting, date) 

painting_dates = list(zip(paintings, dates))

#Assigning the new merged list to the painting list

paintings = painting_dates

#Printing the initial painting list with their dates

print("Initial paintings with their dates: \n")
for painting_values in paintings:
  print(painting_values[0] + " - " + str(painting_values[1]))

#Adding new paintings to the list

new_paintings = [("The Broken Column", 1944), ("The Wounded Deer", 1946), ("Me and My Doll", 1937)]
paintings.extend(new_paintings)

# paintings.append(("The Broken Column", 1944))
# paintings.append(("The Wounded Deer", 1946))
# paintings.append(("Me and My Doll", 1937))

#Printing the new painting list with the addition of new paintings to the list

print("\nThe new painting list with the inclusion of the new paintings: \n")
for painting_values in paintings:
  print(painting_values[0] + " - " + str(painting_values[1]))

#Finding the length of the painting list

painting_length = len(paintings)

#Generating a list of identification numbers for each paintings

audio_tour_number = [num_id for num_id in range(1 , painting_length + 1)]
print(f"\nThe painting IDs are: {audio_tour_number}")

#Creating the master list

def create_master_list():
    master_list = list(zip(audio_tour_number, paintings))
    return master_list

#Displaying the new master list with all paintings, including their IDs, names, and dates

master_loop = create_master_list()

print("\nHere's the master list with all the paintings with their respective IDs: \n")
for master_values in master_loop:
  print(str(master_values[0]) + " - " +  " - ".join(str(string) for string in master_values[1])) #Using the join method to loop through the inner tuple, and convert each of its values to a string to concatenate with the final output


# for painting_values in paintings:
#   print(painting_values[0] + " - " + str(painting_values[1]))

# print(f"All paintings with their respective IDs and dates: {create_master_list()}")

# master_list = list(zip(audio_tour_number, paintings))
# print(master_list)