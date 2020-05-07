#!/usr/bin/python3

# Check for duplicates in the list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


# My solution

for index, char in enumerate(some_list):    # get the index and char
    duplicate = some_list.count(char)       # count the duplicates in the list

    if duplicate > 1:                       # print the duplicate character and show the index
        print(f"{char} appeared in the list in index {index}")

    elif duplicate < 1:
        print("there are no duplicates in the list")

# Solution:

duplicates = []     # declared an empty list

for char in some_list:
    if some_list.count(char) > 1:           # if a char is greater 1
        if char not in duplicates:          # check if char is already stored in list
            duplicates.append(char)         # add it to the list

print(f"\nduplicates in the list:\n{duplicates}")
