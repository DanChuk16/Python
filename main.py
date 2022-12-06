try:
    begin = int(input('Begin:'))
    end = int(input('End:'))

    for item in range(begin, end + 1):
        print(item, end=' ')
        if item % 3 == 0:
            print('fizz', end=' ')
        if item % 5 == 0:
            print('buzz', end=' ')
        print()

except Exception as ex:
    print(f'Error: {ex}')