#!/usr/bin/python3

numbers = [10, 2, 3, 4, 8, 11]

# My solution


def highest_even(lis):
    temp = []
    for num in lis:
        if num % 2 == 0:
            temp.append(num)
            highest = max(temp)
            return highest
    else:
        return 0


result = highest_even(numbers)
print(f"highest even number is {result}")


# Solution

def highest_even_2(lis):
    even = []
    for num in lis:
        if num % 2 == 0:
            even.append(num)
    return max(even)


var = highest_even_2(numbers)
print(f"highest even nuflamber is {var}")
