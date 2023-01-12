try:
    start = int(input('Start: '))
    end = int(input('End: '))
    if start > end:
        start, end = end, start
    print('Prime numbers:', end=' ')
    for number in range(start, end + 1):
        counter = 0
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
        if counter == 2:
            print(number, end=' ')
    print()

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')