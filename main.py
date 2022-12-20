try:
    number = int(input('Number:'))
    for i in range(1, 11):
        print(f'{number} * {i} = {number * i}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')