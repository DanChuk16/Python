try:
    number = int(input('Number: '))
    factorial = 1
    for i in range(1, number + 1):
        print(f'{factorial} * {i} = {factorial * i}')
        factorial *= i

    print(f'{number}! = {factorial}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')