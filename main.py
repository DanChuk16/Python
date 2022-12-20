try:
    begin = int(input('Початок: '))
    end = int(input('Кінець: '))
    if begin > end:
        begin, end = end, begin
    while True:
        number = int(input('Число: '))
        if begin <= number <= end:
            for i in range(begin, end+1):
                if i < number or i > number:
                    print(i, end=" ")
                else:
                    print(f"!{i}!", end=" ")
            break
        else:
            print('Помилка: Число не входить в зазначений діапазон. Повтор операції.')

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')