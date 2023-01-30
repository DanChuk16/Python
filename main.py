try:
    whirlpool = input('Whirlpool: ')
    whirlpool_2 = whirlpool
    whirlpool = list(whirlpool)
    for i in whirlpool:
        if '+' in i:
            whirlpool_2 = whirlpool_2.split('+')
            res = int(int(whirlpool_2[0]) + int(whirlpool_2[1]))
            print(res)
        if '-' in i:
            whirlpool_2 = whirlpool_2.split('-')
            res = int(int(whirlpool_2[0]) - int(whirlpool_2[1]))
            print(res)
        if '*' in i:
            whirlpool_2 = whirlpool_2.split('*')
            res = int(int(whirlpool_2[0]) * int(whirlpool_2[1]))
            print(res)
        if '/' in i:
            whirlpool_2 = whirlpool_2.split('/')
            res = float(float(whirlpool_2[0]) / float(whirlpool_2[1]))
            print(res)

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')