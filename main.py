try:
    number = 0
    while number != 10:
        number += 1
        for i in range(1, 11):
            print(f'{number} * {i} = {number * i}', end='     ')
        print('\n.............................................................................................................................................................')

except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')