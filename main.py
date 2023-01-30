import random
try:
    lengthOfFList = int(input('Length of list: '))
    begin = int(input('Begin: '))
    end = int(input('End: '))
    if begin > end:
        begin, end = end, begin
    numbers = list()
    for i in range(0, lengthOfFList):
        numbers.append(random.randint(begin, end))
    print(numbers)

    count = 0
    count_2 = 0
    count_3 = 0
    #min = min(numbers)
    #max = max(numbers)
    for j in numbers:
        if j < 0:
            count += 1
        if j > 0:
            count_2 += 1
        if j == 0:
            count_3 += 1
    print(f'Min element: {min(numbers)}')
    print(f'Max element: {max(numbers)}')
    print(f'Of all negative elements: {count}')
    print(f'Of all positive elements: {count_2}')
    print(f'All zeros: {count_3}')

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')