try:
    while True:
        money = float(input(f'How much money do you have? '))
        print('#---------------<MENU>---------------#')
        print('|  From which currency to convert?   |')
        print('|  $ : Convert from dollars          |')
        print('|  € : Convert from euros            |')
        print('|  ₴ : Convert from hryvnias         |')
        print('#------------------------------------#')
        action = input('Action:')
        if action == '$':
            dol = float(money * 1)
        if action == '€':
            dol = float(money * 1.06)
        if action == '₴':
            dol = float(money * 0.027)
        print('#--------------<MENU>--------------#')
        print('|  To which currency to convert?   |')
        print('|  $ : Convert to dollars          |')
        print('|  € : Convert to euros            |')
        print('|  ₴ : Convert to hryvnias         |')
        print('#----------------------------------#')
        action = input('Action:')
        if action == '$':
            print(f'Dollars: {dol * 1}')
        if action == '€':
            print(f'Euros: {dol * 0.94}')
        if action == '₴':
            print(f'Hryvnas: {dol * 36.77}')
        act = input('Shall we continue? (Y/N) ')
        if act == 'N':
            break

except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')