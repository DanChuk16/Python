try:
    size = int(input('Size: '))
    for i in range(0, size):
        for a in range(0, size):
            if i == 0 or i == size-1:
                print('*', end='  ')
            else:
                if a == 0 or a == size-1:
                    print('*', end='  ')
                else:
                    print(' ', end='  ')
        print()
except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')
