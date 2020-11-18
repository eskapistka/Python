# This code returns a list of lists. Every list inside the output list contains the same character (all of its occurences in the main input list)

# Expect one input from user
usr_input = input("Enter a list: ")
user_list = usr_input[1:-1].strip().replace(' ', '').replace('"', "'").split(',')
dictionary = {}
output_list = []

for element in user_list:
    if element[:1] and element[-1:] == "'":
        element = element[1:-1]
    else:
        if 96 < ord(element) < 123:
            pass
        else:
            element = int(element)
    if element in dictionary:
        dictionary[element] += 1
    else:
        dictionary[element] = 1

for key in dictionary:
    output_list.append([key] * dictionary[key])

answer = output_list
