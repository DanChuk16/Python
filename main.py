try:
    number = float(input('Number: '))
    if number > 0:
        print('Number is positive')
    elif number < 0:
        print('Number is negative')
    elif number == 0:
        print('Number is equal to zero')
except:
    print('   !!!ERROR!!!   \nYou entered the wrong number!')