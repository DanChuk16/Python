try:
    whirlpool = input('Whirlpool: ')
    whirlpool_2 = whirlpool
    whirlpool = list(whirlpool)
    print(whirlpool)
    for i in whirlpool:
        if '+' in i:
            whirlpool_2 = whirlpool_2.split('+')
            res = int(whirlpool_2.index(0) + whirlpool_2.index(1))
            #index_plus = whirlpool.index('+')
            #num_1 = whirlpool[whirlpool.index(min(whirlpool))-1: index_plus]
        if '-' in whirlpool:
            index_minus = whirlpool.index('-')
        if '*' in whirlpool:
            index_mul = whirlpool.index('*')
        if '/' in whirlpool:
            index_divisi = whirlpool.index('/')
except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')