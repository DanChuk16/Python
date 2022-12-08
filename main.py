try:
    start = int(input('Start:'))
    end = int(input('End:'))
    sum = float(0)
    count = 0
    print('---Couples:')
    for item in range(start, end + 1):
        if item % 2 == 0:
            print(item, end=' ')
            sum += item
            count += 1
    print()
    print('Sum:', sum)
    print(f'Avg: {sum / count}')
    print()
    print('---Odd:')
    sum = float(0)
    count = 0
    for item in range(start, end + 1):
        if item % 2 != 0:
            print(item, end=' ')
            sum += item
            count += 1
    print()
    print('Sum:', sum)
    print(f'Avg: {sum / count}')
    print()
    print('---%9:')
    sum = float(0)
    count = 0
    for item in range(start, end + 1):
        if item % 9 == 0:
            print(item, end=' ')
            sum += item
            count += 1
    print()
    print('Sum:', sum)
    print(f'Avg: {sum / count}')

except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')