try:
    while True:
        x = int(input('X->'))
        y = int(input('Y->'))
        print(pow(x, y))
        question = input('Shall we continue? ')
        if question == 'n' or question == 'N':
            break

except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')