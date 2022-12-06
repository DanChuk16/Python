try:
    begin = int(input('Begin:'))
    end = int(input('End:'))

    for item in range(begin, end + 1):
        if item % 7 == 0:
            print(item, end='\t')
except Exception as ex:
    print(f'Error: {ex}')