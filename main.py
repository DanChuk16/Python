try:
    begin = int(input('Begin:'))
    end = int(input('End:'))

    for item in range(begin, end + 1):
        print(item, end='\t')

    for item in reversed(range(begin, end + 1)):
        print(item, end='\t')

    for item in range(begin, end + 1):
        if item % 7 == 0:
            print(item, end='\t')

    for item in range(begin, end + 1):
        if item % 5 == 0:

except Exception as ex:
    print(f'Error: {ex}')