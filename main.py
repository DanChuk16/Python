try:
    print('#-------------<МЕНЮ>-------------#')
    print('| З якого оператора ви дзвонили: |')
    print('|        *Kyivstar = "K"         |')
    print('|        *Vodafone = "V"         |')
    print('|        *lifecell = "L"         |')
    print('#--------------------------------#')
    action = input('Action: ')
    if action == 'K' or action == 'V' or action == 'L':
        grn = float(input('Напишіть вартість розмови за хвилину оператора (грн): '))
        grn_s = float(grn / 60)
    else:
        raise Exception('Ви не вибрали один із заданих варіантів!')
    print('Скільки часу ви говорили?')
    h = int(input('Годин: '))
    if h < 0:
        raise Exception('Помилка! Це число є відʼємним')
    m = int(input('Хвилин: '))
    if m > 60:
        raise Exception('Помилка! Ви ввели хвилин більше за 60 (бо це вже 1 година)')
    elif m < 0:
        raise Exception('Помилка! Це число є відʼємним')
    s = int(input('Секунд: '))
    if s > 60:
        raise Exception('Помилка! Ви ввели секунл більше за 60 (бо це вже 1 хвилина')
    elif s < 0:
        raise Exception('Помилка! Це число є відʼємним')
    h_2 = int(h * 3600)
    m_2 = int(m * 60)
    cost = float((h_2 + m_2 + s) * grn_s)
    print(f'Вартість розмови: {cost} гривень')
except Exception as ex:
    print(f'{ex}')