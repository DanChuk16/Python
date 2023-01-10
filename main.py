try:
    size = int(input('Size: '))
    for i in range(1, size + 1):
        for a in range(1, size + 1):
            if i == 0:
                print('*', end=' ')
            else:
                if a == 0:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
        print()
except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')
