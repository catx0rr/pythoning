''' 
	Password checker using len function
'''

user_name = input('Enter username: ')
passwd = input('Enter password: ')
passwd_mask = '*' * len(passwd)
passwd_length = len(passwd)


''' using fstring formatting '''
print(f'Hello {user_name}, your password {passwd_mask} is {passwd_length} characters long')