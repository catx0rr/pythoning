#!/usr/bin/python3

'''
    Make a list of five or more usernames, including the name 'admin'. 
    Imagine you are writing code that will print a greeting to each user 
    after they log in to a website. Loop through the list, and print a greeting 
    to each user:

'''

# Solution

usernames = [
    'admin',
    'weber',
    'janix',
    'geoff'
]

if usernames:
    for username in usernames:
        if username is 'admin':
            print(f'Welcome {username}. Do you want to print a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again.')
else:
    print('Username not found.')


'''
   Make a list of five or more usernames called current_users.
   Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the 
   current_users list. 

   Loop through the new_users list to see if each new username has already been used. 
   If it has, print a message that the person will need to enter a new username. If a username has not been used, 
   print a message saying that the username is available. Make sure your comparison is case insensitive. 
   If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users 
   containing the lowercase versions of all existing users.)

'''
current_users = ['arvin', 'kelvin', 'foster', 'john', 'doe']
new_users = ['john', 'doe', 'harvey', 'hoit', 'raz']


for user in new_users:
    if user.casefold() in current_users:
        print(f'{user} not available ')
    else:
        print(f'{user} is available')
