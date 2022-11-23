try:
    manager_1 = float(input('Manager_1: '))
    manager_2 = float(input('Manager_2: '))
    manager_3 = float(input('Manager_3: '))
    if manager_1 < 500:
        salry_1 = float(manager_1 * 3 / 100 + 200)
    elif manager_1 > 500 and manager_1 < 1000:
        salry_1 = float(manager_1 * 5 / 100 + 200)
    elif manager_1 > 1000:
        salry_1 = float(manager_1 * 8 / 100 + 200)
    else:
        raise Exception('You typed something wrong!')

    if manager_2 < 500:
        salry_2 = float(manager_2 * 3 / 100 + 200)
    elif manager_2 > 500 and manager_2 < 1000:
        salry_2 = float(manager_2 * 5 / 100 + 200)
    elif manager_2 > 1000:
        salry_2 = float(manager_2 * 8 / 100 + 200)
    else:
        raise Exception('You typed something wrong!')

    if manager_3 < 500:
        salry_3 = float(manager_3 * 3 / 100 + 200)
    elif manager_3 > 500 and manager_3 < 1000:
        salry_3 = float(manager_3 * 5 / 100 + 200)
    elif manager_3 > 1000:
        salry_3 = float(manager_3 * 8 / 100 + 200)
    else:
        raise Exception('You typed something wrong!')

    if salry_1 > salry_2 and salry_1 > salry_3:
        salry_1 = float(salry_1 + 200)
    elif salry_2 > salry_1 and salry_2 > salry_3:
        salry_2 = float(salry_2 + 200)
    elif salry_3 > salry_1 and salry_3 > salry_2:
        salry_3 = float(salry_3 + 200)
    else:
        print('There is no best manager!')

    print(f'\tSALARY:\nManager_1: {salry_1}$\nManager_2: {salry_2}$\nManager_3: {salry_3}$')
except Exception as ex:
    print(f'Error: {ex}')