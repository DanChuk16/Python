try:
    number = 0
    sum = 0
    min = 0
    max = 0
    trigger = True
    while True:
        number = int(input('Number: '))
        if number == 7:
            break
        else:
            sum += number
            if trigger:
                min = max = number
                trigger = False
            else:
                if max < number:
                    max = number
                if min > number:
                    min = number
    print(f'Sum: {sum}')
    print(f'Max: {max}')
    print(f'Min: {min}')
    print('Good bye!')

except Exception as ex:
    print(ex)