#!/usr/bin/python3

def multiply(param1, param2):
    return param1 * param2


def divide(param1, param2):
    if param2 != 0:
        return param1 / param2
    else:
        return "cannot divided by 0"


def add(param1, param2):
    return param1 + param2


def subtract(param1, param2):
    return param1 - param2


# Calculator function
def calculator(param1, param2, operator):
    result = operator(param1, param2)
    return result


result = calculator(5, 15, subtract)
print(result)
