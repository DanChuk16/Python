try:
    number = int(input('Number->'))
    if number > 100 or number < 0:
        raise Exception('You did not enter a number from 1 to 100!')

    if number % 3 == 0 and number % 5 != 0:
        print('Fizz')
    elif number % 5 == 0 and number % 3 != 0:
        print('Buzz')
    elif number % 3 == 0 and number % 5 == 0:
        print('Fizz Buzz')
    elif number % 3 != 0 and number % 5 != 0:
        print(number)
except Exception as ex:
    print(f'Error: {ex}')