try:
    num = input('Numbers: ').split()
    Sum = 0
    count = 0
    for i in num:
        if i.isnumeric():
            Sum += i
            count += 1
    print(f'Sum: {Sum}')
    print(f'Avg: {Sum/count}')

except Exception as ex:
    print(f'Error: {ex}')