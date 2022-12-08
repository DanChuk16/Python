try:
    number = int(input('Number: '))
    for i in range(1, number + 1):
        print('*', end= ' ')

except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')