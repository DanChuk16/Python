try:
    width = int(input('Width: '))
    height = int(input('Height: '))
    for i in range(1, width + 1):
        for a in range(1, height + 1):
            print('*', end=' ')
        print()
except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')
