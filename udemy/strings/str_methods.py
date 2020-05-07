#!/usr/bin/python3

''' string methods '''

# .title() method
#
# capitalizes each word begins with capital letter

name_t = "ada lovelace"
print(name_t.title())


# .upper() and #.casefold() method
#
# turns strings all caps or small caps

name_u = "ada lovelace"
print(name_u.upper())

name_c = "ada lovelace"
print(name_c.casefold())


# string formatting (f-strings)

f_name = "ada"
l_name = "lovelace"
full_name = f"{f_name} {l_name}".title()
print(f"Hello, {full_name}!")


# tabs and newlines \n \t
message = "Languages:\n\tPython\n\tC++\n\tJavascript"
print(message)


# .strip() methods
fav_language = " python "
print(fav_language.rstrip())
print(fav_language.lstrip())
print(fav_language.strip())
