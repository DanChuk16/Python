try:
    string = input('String: ')
    symbol = input('Symbol: ')
    counter = 0
    for i in string:
        if i == symbol:
            counter += 1
    print(f'The symbol appears {counter} times')

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')