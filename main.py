try:
    whirlpool = input('Whirlpool: ')
    whirlpool = list(whirlpool)
    print(whirlpool)


except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')