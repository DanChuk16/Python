number_1 = int(float(input('Number 1 = ')))
number_2 = int(float(input('Number 2 = ')))
print('#-----------------<Menu>-----------------#')
print(f'|      +: Show sum for {number_1} and {number_2}           |')
print(f'|      -: Show difference for {number_1} and {number_2}    |')
print(f'|      *: Show product for {number_1} and {number_2}       |')
print(f'|    avg: Show avg for {number_1} and {number_2}           |')
print('#----------------------------------------#')
action = input('Action: ')
if action == '+':
    print(f'{number_1} + {number_2} = {number_1 + number_2}')
elif action == '-':
    if number_1 >= number_2:
        print(f'{number_1} - {number_2} = {number_1 - number_2}')
    elif number_1 <= number_2:
        print(f'{number_2} - {number_1} = {number_2 - number_1}')
elif action == '*':
    print(f'{number_1} * {number_2} = {number_1 * number_2}')
elif action == 'avg':
    print(f'({number_1} + {number_2})/2 = {(number_1 + number_2)/2}')