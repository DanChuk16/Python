try:
    number = int(input('Number: '))
    print('#---------<MENU>---------#')
    print(f'|   "0" : Show {number} ** 0    |')
    print(f'|   "1" : Show {number} ** 1    |')
    print(f'|   "2" : Show {number} ** 2    |')
    print(f'|   "3" : Show {number} ** 3    |')
    print(f'|   "4" : Show {number} ** 4    |')
    print(f'|   "5" : Show {number} ** 5    |')
    print(f'|   "6" : Show {number} ** 6    |')
    print(f'|   "7" : Show {number} ** 7    |')
    print('#------------------------#')
    action = input('Action: ')
    if action == '0':
        print('Reply:', int(number ** 0))
    elif action == '1':
        print('Reply:', int(number ** 1))
    elif action == '2':
        print('Reply:', int(number ** 2))
    elif action == '3':
        print(int(number ** 3))
    elif action == '4':
        print(int(number ** 4))
    elif action == '5':
        print(int(number ** 5))
    elif action == '6':
        print(int(number ** 6))
    elif action == '7':
        print(int(number ** 7))
    else:
        print('You did not enter a number for 1 to 7!')
except:
    print('   !!!ERROR!!!\nYou entered something wrong!   ')