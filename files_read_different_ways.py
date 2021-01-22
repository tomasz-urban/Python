with open('test.txt') as my_file:
    print(my_file.read())

# Some other way to do this (worse way):

# my_file = open('test.txt')
# print(my_file.read())

###########################################################################
# open reads file only once and moves cursor to the end of file
# to read file again we have to move cursor to the beginning of file using:
###########################################################################

# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
#
# my_file.close()

# .readline() - reading by line
# .readlines() - read all lines as a list with "/n"



