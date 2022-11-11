try:
    number_1 = float(input('Number 1: '))
    number_2 = float(input('Number 2: '))
    if number_1 == number_2:
        print('These numbers are equal!')
    elif number_1 > number_2:
        print(f'{number_2}, {number_1}')
    elif number_1 < number_2:
        print(f'{number_1}, {number_2}')
except:
    print('   !!!ERROR!!!   \nYou did something wrong!')