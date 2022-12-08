try:
    start = int(input('Start:'))
    if start == 7:
        raise Exception('Good bye!')
    end = int(input('End:'))
    if end == 7:
        raise Exception('Good bye!')
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        if i > 0:
            print(i, 'Number is positive')
        if i < 0:
            print(i, 'Number is negative')
        if i == 0:
            print(i, 'Number is equal to zero')

except Exception as ex:
    print(ex)