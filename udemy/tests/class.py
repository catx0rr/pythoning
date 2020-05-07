#!/usr/bin/python3

# My solution

# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("moewy", 3)
cat2 = Cat("mingming", 2)
cat3 = Cat("fuckingcat", 4)

cats = {
    cat1.name: cat1.age,
    cat2.name: cat2.age,
    cat3.name: cat3.age
}

# 2 Create a function that finds the oldest cat


def get_oldest(dictionary):
    cat_age = []
    for name, age in cats.items():
        cat_age.append(age)

        for age in cat_age:
            return max(cat_age)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f" the cat with the age of {get_oldest(cats)} is the oldest.")


# Solution

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")
