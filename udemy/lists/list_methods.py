#!/usr/bin/python3

sch_items = [
    'notebook',
    'laptop',
    'pen',
    'paper'
]

''' list access '''
print(sch_items[0])

''' list copy '''

sch_items1 = sch_items[:]
print(sch_items1)

''' list mutate '''

sch_items1[3] = 'yellow paper'
print(sch_items1)

# Methods

''' adding '''
sch_items1.append('binder')
print(sch_items1)

''' popping a list '''
# pop can be reused when passsed into a variable
sch_items1.pop(0)
print(sch_items1)

''' copying and appending to the copied list'''

sch_items2 = sch_items1[:]
sch_items2.append('pencil')
print(sch_items2)

''' remove from a list '''
# remove is totally removing the item on the list
sch_items2.remove('pencil')
print(sch_items2)  # removing the item named 'pencil'

''' clearing the list '''

sch_items2.clear()
print(sch_items2)
