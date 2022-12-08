try:
    start = int(input('Start: '))
    end = int(input('End: '))
    sum = float(0)
    counter = 0
    for i in range(start, end + 1):
        print(f'{sum} + {i} = {sum + i}')
        sum += i
        counter += 1
    print(f'Sum = {sum}\nAvg = {sum/counter}')
except Exception as ex:
    print(f'Error: {ex}')