try:
    start = int(input('Start: '))
    end = int(input('End: '))
    number = 0
    if start > end:
        start, end = end, start
    while number != 10:
        number += 1
        for i in range(start, end + 1):
            print(f'{i} * {number} = {number * i}', end='    ')
        print()#'\n.........................................................................................................................................................')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')