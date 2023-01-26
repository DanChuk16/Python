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
    counter = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 1

    for j in numbers:
        if j < 0:
            counter += j
        if j % 2 == 0:
            counter_2 += j
        if j % 2 != 0:
            counter_3 += j

    for a in range(0, lengthOfFList):
        if a % 3 == 0:
            counter_4 *= numbers[a]
    partList = numbers[numbers.index(max(numbers))+1: numbers.index(min(numbers))].copy()
    mul = 1
    for item in partList:
        mul *= item
    #partlist = numbers[numbers.index()]
    #sum = 0
    #for it in partlist:
        #sum += it

    print(f'Sum negative numbers: {counter}')
    print(f'Sum even numbers: {counter_2}')
    print(f'Sum odd numbers: {counter_3}')
    print(f'Product of numbers that are multiples of 3: {counter_4}')
    print(f'The product of elements between the minimum and maximum element: {mul}')
    print()
    print()

    print('Even numbers:')
    for j in numbers:
        if j % 2 == 0:
            print(j, end=' ')
    print()
    print('Odd numbers:')
    for j in numbers:
        if j % 2 != 0:
            print(j, end=' ')
    print()
    print('Negative numbers:')
    for j in numbers:
        if j < 0:
            print(j, end=' ')
    print()
    print('Positive numbers:')
    for j in numbers:
        if j > 0:
            print(j, end=' ')

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')