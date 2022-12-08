try:
    begin = int(input('Begin:'))
    end = int(input('End:'))

    for item in range(begin, end + 1):
        print(item, end=' ')
    print()


    for item in reversed(range(begin, end + 1)):
        print(item, end=' ')
    print()


    for item in range(begin, end + 1):
        if item % 7 == 0:
            print(item, end=' ')
    print()

    counter = 0
    for item in range(begin, end + 1):
        if item % 5 == 0:
            counter += 1
    print(counter)


except Exception as ex:
    print(f'Error: {ex}')