try:
    from datetime import datetime
    fixTime1 = datetime.now()
    counter = 0
    print('-----<Вгадай число>-----')
    import random
    number = random.randint(1, 500)
    while True:
        number_1 = int(input('Число:'))
        if number_1 > number and number_1 <= 500:
            print('---Число МЕНШЕ')
            counter += 1
        elif number_1 < number and number_1 >= 1:
            print('---Число БІЛЬШЕ')
            counter += 1
        elif number_1 == number:
            print('---ВГАДАЛИ!!! ВІТАЮ!---')
            counter += 1
            break
        elif number_1 < -1 or number_1 > 500:
            print('Ви не ввели число у діапазоні: 1-500')
            counter += 1
        if number_1 == 0:
            break
    fixTime2 = datetime.now()
    print()
    print(f'Всього зайняло часу: {fixTime2 - fixTime1}')
    print(f'Всього спроб: {counter}')
except Exception as ex:
    print(f'Помилка: [{ex.__class__.__name__}]: {ex}')