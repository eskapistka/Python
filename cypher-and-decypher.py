# cw2.py (template file)

import csv


# =============================================================================
# (a) Key checker function
# This function checks if the key is between 0 and 94.
# =============================================================================
def check_key(key):
    # Replace the following lines with your code
    if key in range(0, 95):
        return True
    return False


# =============================================================================
# (b) Function to count number of upper case and lower case letters
# This function counts the number of upper case and lower case letter of a
# given string.
# =============================================================================

def check_upper_lower(s):
    upper = 0
    lower = 0

    for char in s:
        if char.islower():
            lower = lower + 1
        if char.isupper():
            upper = upper + 1

    return [upper, lower]


# =============================================================================
# (c) Function to encrypt or decrypt a string
# Encrypt or decrypt a string s1 with a key based on the option
# and return a string value.
# Option = 1 for encrypt, option =2 for decrypt, default option =1,
# other option value returns message "Invalid option!".
# Key value between 0 and 94, default key=3. Other key value returns
# "Invalid key!"
# =============================================================================
def encrypt_decrypt_string(s1, key=3, option=1):
    # For invalid option
    if option != 1 and option != 2:
        output = "Invalid option!"
        return output
    # For invalid key
    if check_key(key) is False:
        output = "Invalid key!"
        return output

    # I initialize output as an empty string
    output = ''
    # Decryption (option 2) is just reversed encryption (option 1 - default)
    if option == 2:
        key = -key

    for char in s1:
        if 32 <= ord(char) <= 126:
            if (ord(char) + key) > 126 or (ord(char) + key) < 32:
                output += chr(((ord(char) + key) % 127) + 32)
            else:
                output += chr(ord(char) + key)
        else:
            output += char

    return output


# This is an example of how to call this function without providing key argument
# print(encrypt_decrypt_string('Khoor#Zruog#=,', option = 2))
# Calling this function without the option argument
# print(encrypt_decrypt_string('Khoor#Zruog#=,', 3))

# =============================================================================
# (d) Function to encrypt or decrypt content of a text file
# Encrypt and decrypt a txt file (infile) based on the key and option, call to
# function in part (c) to encrypt each string in the file. Output the encrypted
# string to a different txt file (outfile) and print "Wrong file or file path"
# if infile is not found. Do not forget the default key and option as in (c).
# =============================================================================

def encrypt_decrypt_text_in_file(infile, outfile, key=3, option=1):
    try:
        in_file = open(infile, 'r').readlines()
        # I want to have every line as a separate item in an array, I get rid of "\n" escape char
        in_file = [x.replace('\n', '') for x in in_file]
        # I create output txt file with the name and extension of outfile function argument
        out_file = open(str(outfile), 'w+')

        # The if statement is here, because the test recognises "\n" escape char and fails because of that
        for i in range(0, len(in_file)):
            out_file.write(str(encrypt_decrypt_string(in_file[i], key, option)))
            if i < len(in_file) - 1:
                out_file.write('\n')

    except (FileNotFoundError, IOError):
        print("Wrong file or file path")


encrypt_decrypt_text_in_file('input.txt', 'output.txt', 3, 1)


# =============================================================================
# (e) Function to count occurrence of words in a text file
# This function count the occurrences of each word in a txt file (sfile) and
# returns the occurences of each word in a dictionary format. It returns
# "Wrong file or file path" if sfile is not found.
# =============================================================================
def count_words_in_file(sfile):
    # Key to the dictionary is the word in uppercase and the value is the number of its occurences
    wordlist = {}
    try:
        # I want to have every line of input as a different element in the array
        in_file = open(sfile, 'r').readlines()

        # I want to get rid of different characters from the input
        characters = ['\n', ',', '.', '?', '!']
        for char in characters:
            in_file = [x.replace(char, '') for x in in_file]
        # I split every line of the input file into an array of words
        in_file = [x.split() for x in in_file]

        for line in in_file:
            for word in line:
                word = word.upper()
                if word not in wordlist:
                    wordlist[word] = 1
                else:
                    wordlist[word] += 1

        return wordlist

    except (FileNotFoundError, IOError):
        return "Wrong file or file path"


# =============================================================================
# (f) Function to find max, min, sum, count, and mean
# (Not required for COMP0011 (IFY) students)
# This function find the maximum, minimum, sum, count, and mean values of
# a column (as specified by col_index) in a txt file (infile). Note that
# col_index starts with a 0 (zero).
# =============================================================================
def summarise_data(infile, col_index):
    try:
        with open(infile) as input_file:
            reader = csv.reader(input_file)
            # I want to check the numbers of columns by checking the length of the first row (it's a list)
            for row in reader:
                columns_number = len(row)
                if col_index > columns_number - 1:
                    return 'Invalid index'

                col_maximum = 0
                col_minimum = 0
                col_sum = 0
                count = 0

                # It's there so the rest of the code doesn't miss the first row
                # I check for an empty value in the first if
                # Then I check if the value is of int type
                if row[col_index] != '':
                    if type(int(row[col_index])) is int:
                        col_maximum = int(row[col_index])
                        col_minimum = col_maximum
                        col_sum += int(row[col_index])
                        count += 1
                break
            for row in reader:
                if row[col_index] != '':
                    if type(int(row[col_index])) is int:
                        if int(row[col_index]) > col_maximum:
                            col_maximum = int(row[col_index])
                            if col_minimum == 0:
                                col_minimum = col_maximum
                        if int(row[col_index]) < col_minimum:
                            col_minimum = int(row[col_index])
                        col_sum += int(row[col_index])
                        count += 1

            col_mean = col_sum / count

        results = [col_maximum, col_minimum, col_sum, count, round(col_mean, 2)]

    except (FileNotFoundError, IOError):
        return "Wrong file or file path"

    return results
