#!/usr/bin/python3

''' list index '''

items = [
	'a',
	'b',
	'c',
	'x',
	'd',
	'e'
]


print(items.index('a')) # will print 0

''' count method '''

print(items.count('d')) # will print how many times occurred

''' sort method '''
items.sort() # modifying the list
#print(items) # will sort the list
# or use sorted

print(sorted(items)) # create a new sorted item that can be passed to a variable


