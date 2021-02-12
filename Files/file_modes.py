with open('sad.txt', mode='w') as my_file:
    text = my_file.write(':(')
    print(text)

# with 'r' mode we only read file
# with 'w' mode we create a new file or overwrite existing with the same name (removing everything from the file!!!)
# with 'a' mode we append at the end of file
# with 'r+' mode we write sth at the beginning of the file (overwriting what is at the beginning)

