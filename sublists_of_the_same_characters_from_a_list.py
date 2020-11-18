# This code prints a list of lists, every list in the output list contains
# every occurrence of the same character, note that '1' is different than 1

def list_of_lists(input_list):
    input_list = str(input_list)
    user_list = input_list[1:-1].strip().replace(' ', '').replace('"', "'").split(',')
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

    return output_list

# Simple test for the function (using pytest)

def test_answer():
    assert list_of_lists([2, 1, 2, 1]) == [[2, 2], [1, 1]]
    assert list_of_lists([5, 4, 5, 5, 4, 3]) == [[5, 5, 5], [4, 4], [3]]
    assert list_of_lists([2,1,2,1]) == [[2, 2], [1, 1]]
    assert list_of_lists([1,2,1,3,'a','b',"a", 'c', 'a',"a", "a", '1',"1"]) == [[1, 1], [2], [3], ['a', 'a', 'a', 'a', 'a'], ['b'], ['c'], ['1', '1']]
