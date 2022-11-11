try:
    number = int(input('Number->'))
    if number == 1:
        print('Monday')
    elif number == 2:
        print('Tuesday')
    elif number == 3:
        print('Wednesday')
    elif number == 4:
        print('Thursday')
    elif number == 5:
        print('Friday')
    elif number == 6:
        print('Saturday')
    elif number == 7:
        print('Sunday')
    else:
        print('It is not a day of the week. There are only 7 days in a week.')
except:
    print('   !!!ERROR!!!   \nYou entered incorrect data!')