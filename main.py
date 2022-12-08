try:
    number = int(input('Number: '))
    symbol = input('Symbol: ')
    for i in range(1, number + 1):
        print(symbol)

except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')