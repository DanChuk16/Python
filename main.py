try:
    length = int(input('Length: '))
    width = int(input('Width: '))
    for i in range(0, length):
        for a in range(0, width):
            if i == 0 or i == length-1:
                print('*', end=' ')
            else:
                if a == 0 or a == width-1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
        print()
except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')
