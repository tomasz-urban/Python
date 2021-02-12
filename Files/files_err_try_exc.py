try:
    with open('sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('File does not exist')
    raise err  # this shows the error not only print text above
