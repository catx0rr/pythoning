user = {
    'name': 'Aster',
    'age': 21,
    'address': '81 Arctic St Florida',
    'email': 'aster@email.com',
}

# iterate and get the keys
for key in user.keys():
    print(key)

# using get method
for key in user.get():
    print(key)

# iterate and get the values
for value in user.values():
    print(value)

# iterate and get the tuple in each items
for item in user.items():
    print(item)

# iterate unpack the tuple
for key, value in user.items():
    print(f"{key}: {value}")


for key in user.get():
    print(key)
