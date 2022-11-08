meters = float(input('Meters: '))
print('#------------------>Menu<------------------#')
print(f'|    mil : Convert {meters} meters to miles     |')
print(f'|   inch : Convert {meters} meters to inches    |')
print(f'|   yard : Convert {meters} meters to yards     |')
print('#------------------------------------------#')
action = input('Action: ')
if action == 'mil':
    print(f'{meters} meters = {meters * 0.000621371192} miles')
elif action == 'inch':
    print(f'{meters} meters = {meters * 39.3700787} inches')
elif action == 'yard':
    print(f'{meters} meters = {meters * 1.0936133} yards')
else:
    print('Command not found!')