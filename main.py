try:
    num = list()
    lenght = int(input('Size: '))
    for i in range(1, lenght + 1):
        num.append(int(input(f'item[{i}]: ')))
    print(num)
    Sum = 0
    count = float(0)
    for i in num:
      Sum += i
    print(f'Sum: {Sum}')
    print(f'Avg: {Sum/lenght}')

except Exception as ex:
    print(f'Error: {ex}')