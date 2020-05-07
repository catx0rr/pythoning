#!/usr/bin/python3

# i = 0

# while i < 50:
#     print(i)
#     i += 1

# print("done")

''' Input with response using while loop'''

while True:
    response = input("Say something: ")

    if response == "bye":
        break

    print(f"You typed: {response}")
