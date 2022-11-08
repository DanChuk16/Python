number_1 = float(input('Nimber 1 = '))
number_2 = float(input('Nimber 2 = '))
number_3 = float(input('Nimber 3 = '))
print('#--------------------->Menu<---------------------#')
print(f'|  max : Show maximum between {number_1}, {number_2} and {number_3}   |')
print(f'|  min : Show minimum between {number_1}, {number_2} and {number_3}   |')
print(f'|  avg : Show avg for {number_1}, {number_2} and {number_3}           |')
print('#------------------------------------------------#')
action = input('Action: ')
if action == 'max':
    if number_1 >= number_2 and number_1 >= number_3:
        print(f'Max is {number_1}')
    elif number_2 >= number_1 and number_2 >= number_3:
        print(f'Max is {number_2}')
    elif number_3 >= number_1 and number_3 >= number_2:
        print(f'Max is {number_3}')
    else:
        print(f'All values is equal!')
elif action == 'min':
    if number_1 <= number_2 and number_1 <= number_3:
        print(f'Min is {number_1}')
    elif number_2 <= number_1 and number_2 <= number_3:
        print(f'Min is {number_2}')
    elif number_3 <= number_1 and number_3 <= number_2:
        print(f'Min is {number_3}')
    else:
        print(f'All values is equal!')
elif action == 'avg':
    print(f'Avg = ({number_1} + {number_2} + {number_3})/3 = {(number_1 + number_2 + number_3)/3}')
else:
     print('Command not found!')