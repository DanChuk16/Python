number_1 = float(input('Number 1 = '))
number_2 = float(input('Number 2 = '))
number_3 = float(input('Number 3 = '))
print('#------------------<Menu>------------------#')
print(f'|   + : Show sum for {number_1}, {number_2} and {number_3}      |')
print(f'|   * : Show product for {number_1}, {number_2} and {number_3}  |')
print('#----------------------------------------#')
action = input('Actoin: ')
if action == '+':
    print(f'{number_1} + {number_2} + {number_3} = {number_1 + number_2 + number_3}')
elif action == '*':
    print(f'{number_1} * {number_2} * {number_3} = {number_1 * number_2 * number_3}')
else:
    print('Command not found!')