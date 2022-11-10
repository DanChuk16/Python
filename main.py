try:
    diameter = float(input('Diameter: '))
    print('#------------->MENU<-------------#')
    print('|   a : Show area circle         |')
    print('|   p : Show perimeter circle    |')
    print('#--------------------------------#')
    action = input('Actoin: ')
    if action == 'a':
        print(f'Area = ({diameter} ** 2 * Pi) / 4 = {(diameter ** 2 * 3.14) / 4}')
    elif action == 'p':
        print(f'Perimeter = {diameter} * Pi = {diameter * 3.14}')
    else:
        print(' You did not select a given option')
except:
    print('   !!!ERROR!!!   \nYou entered something wrong!')