try:
    whirlpool = input('Whirlpool: ')
    whirlpool = list(whirlpool)
    print(whirlpool)
    for i in whirlpool:
        if '+' in i:
            index_plus = whirlpool.index('+')

        elif '-' in whirlpool:
            index_minus = whirlpool.index('-')
        elif '*' in whirlpool:
            index_mul = whirlpool.index('*')
        elif '/' in whirlpool:
            index_divisi = whirlpool.index('/')

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')