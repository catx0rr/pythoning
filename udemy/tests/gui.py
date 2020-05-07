#!/usr/bin/python3

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],

]

# shorter and cleaner code

for row in picture:           # loops into the list picture
    for pixel in row:         # loops in the 1st item in the picture
        if pixel != 0:          # check for not 0, and change it to * char
            pixel = '*'
        else:                   # else, if 0 change it to a space
            pixel = ' '
        print(pixel, end='')    # print the image
    print(end='\n')             # add a new line after looping in the first item in list


# or use replace function


for row in picture:                           # loops into the list picture
    for pixel in row:                         # loops in the 1st item in the picture
        if pixel != 0:                          # check for not 0, and change it to * char
            string = str(pixel)
            result = string.replace("1", '*')
            print(result, end='')               # print the image
        else:                                   # else, if 0 change it to a space
            string = str(pixel)
            result = string.replace("0", ' ')
            print(result, end='')               # print the image

    print(end='\n')                             # add a new line after looping in the first item in list
