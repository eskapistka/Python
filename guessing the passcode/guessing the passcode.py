# This code tries to guess the passcode given the data on successful logins The data on successful logins is in form
# of 3 characters that are always asked for in order For a successful login data example would be if the passcode was
# 531278 then the 2nd 3rd and 5th characters would be 317
# This code works for codes with just one apperance of each character, because it is based on
# statistical approach on the most common place the character is

from collections import defaultdict

d = open('data.txt', 'r').readlines()
out = open('data_no_repetition.txt', 'w')

data = [x.replace('\n', "") for x in d]

data_no_repetition = list(dict.fromkeys(data))

for x in data_no_repetition:
    out.write(x)
    out.write('\n')

attempts = []
appearances = defaultdict(list)

for attempt in data_no_repetition:
    attempt = ''.join(attempt.split(' '))
    attempts.append(attempt)

for attempt in attempts:
    for i, n in enumerate(attempt):
        appearances[n].append(i)

average_positions = {}
for k, v in list(appearances.items()):
    average_positions[k] = float(sum(v))/float(len(v))

a = [k for k,v in sorted(list(average_positions.items()), key=lambda a: a[1])]
print(''.join(str(x) for x in a))
