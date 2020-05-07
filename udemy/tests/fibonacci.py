#!/usr/bin/python3


''' functionized '''


def fibo_generator(number):
    fibo = []

    if not number or int(number) <= 0:
        return 0

    elif int(number) == 1:
        fibo.append(0)
        return fibo

    elif int(number) == 2:
        fibo.append(0)
        fibo.append(1)
        return fibo

    else:

        # initialize
        fibo.append(0)
        fibo.append(1)

        # using while loop
        # count = 2
        # while count < int(number):
        #     result = fibo[-2] + fibo[-1]
        #     fibo.append(result)
        #     count += 1
        # print(fibo)

        # using for loop and range function
        for num in range(2, int(number)):
            result = fibo[-2] + fibo[-1]
            fibo.append(result)
        return fibo


fibo_output = fibo_generator('')
print(fibo_output)
''' fibonacci numbers '''

# prompt = "Enter a number: "

# number = input(prompt)

# if not number or int(number) == 0:
#     print("incorrect values")

# elif int(number) == 1:
#     fibo = []
#     fibo.append(0)
#     print(fibo)

# elif int(number) == 2:
#     fibo = []
#     fibo.append(0)
#     fibo.append(1)
#     print(fibo)

# else:
#     fibo = []
#     fibo.append(0)
#     fibo.append(1)
#     count = 2
#     while count < int(number):
#         result = (fibo[-2]) + (fibo[-1])
#         fibo.append(result)
#         count += 1
#     print(fibo)
