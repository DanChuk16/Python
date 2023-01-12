try:
    string = input('String: ')
    counter = 0
    counter_2 = 0
    for i in string:
        if i.isalpha():
            counter += 1
    for j in string:
        if j.isdigit():
            counter_2 += 1
    print(f'Number of letters: {counter}')
    print(f'Number of digits: {counter_2}')

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')