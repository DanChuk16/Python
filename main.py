try:
    string = input('String: ')
    word = input('Word: ')
    counter = 0
    x = string.split()
    for i in x:
        if word in i:
            counter += 1
    print(f'The word appears {counter} times')

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')