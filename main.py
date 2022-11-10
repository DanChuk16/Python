try:
    diameter = float(input('Diameter: '))
    print('#-------------->MENU<--------------#')
    print('|   area : Show area circle        |')
    print('|    per : Show perimeter circle   |')
    print('#----------------------------------#')
    action = input('Actoin: ')
    if action == 'area':
        print(f'Area = ({diameter} ** 2 * Pi) / 4 = {(diameter ** 2 * 3.14) / 4}')
    elif action == 'per':
        print(f'Perimeter = {diameter} * Pi = {diameter * 3.14}')
    else:
        print(' You did not select a given option')
except:
    print('You entered something wrong')