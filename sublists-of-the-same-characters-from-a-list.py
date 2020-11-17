# cw16.py (template file)
print("Print sublists of a list.")

# Expect one input from user
usr_input = input("Enter a list: ")

# Delete the following line and write your own code here
user_list = usr_input[1:-1].strip().replace(' ', '').replace('"', "'").split(',')
print(user_list)
dictionary = {}
output_list = []

for element in user_list:
    if element[:1] and element[-1:] == "'":
        element = element[1:-1]
        #if 96 < ord(element[1:-1]) < 123:
        #    element = element[1:-1]
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

# my own test values for type 3 [1,2,1,3,'a','b',"a", c, 'a',a, "a", '1',"1"]

print(answer)

# You can test your program
# user enter "[2, 1, 2, 1]" expected output [[2, 2], [1, 1]]
# user enter "[5, 4, 5, 5, 4, 3]" expected output [[5, 5, 5], [4, 4], [3]]
# user enter "[2,1,2,1]" expected output [[2, 2], [1, 1]]
