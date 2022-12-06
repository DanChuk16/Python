try:
    begin = int(input('Begin:'))
    end = int(input('End:'))

    for item in reversed(range(begin, end + 1)):
        print(item, end='\t')
except Exception as ex:
    print(f'Error: {ex}')