try:
    one_game_console = float(input('One game console is worth: '))
    number = int(input('Number: '))
    discount = int(input('Discount (%): '))
    print('#------------------>MENU<------------------#')
    print('|   gen : Show general sum                 |')
    print('|   one : Show sum one console (with %)    |')
    print('#------------------------------------------#')
    action = input('Action: ')
    if action == 'gen':
        a = float((one_game_console * number * discount) / 100)
        print(f'General sum = {(one_game_console * number) - a}')
    elif action == 'one':
        b = float((one_game_console * discount) / 100)
        print(f'Sum one console with % = {one_game_console - b}')
    else:
        print('You did not select a given option')
except:
    print('You did something wrong!')