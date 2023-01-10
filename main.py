try:
    size = int(input('Size: '))
    for i in range(1, size + 1):
        for a in range(1, size + 1):
            print('*', end=' ')
        print()
except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')
