import random
try:
    length = int(input("Length of list: "))
    list1 = []
    list2 = []
    if length > 0:
        for i in range(length):
            list1.append(random.randint(-50, 50))
            list2.append(random.randint(-50, 50))
        print(f'List 1: {list1}')
        print(f'List 2: {list2}')
        list3 = list1 + list2
        print(f'1) Elements of both lists: {list3}')
        list3 = list(set(list1 + list2))
        print(f'2) Elements of both lists without repetitions: {list3}')
        list3 = list(set(list1) & set(list2))
        print(f'3) Elements common to the two lists: {list3}')
        list3 = list(set(list1) ^ set(list2))
        print(f'4) Only the unique elements of each of the lists: {list3}')
        list3 = [min(list1), max(list1), min(list2), max(list2)]
        print(f'5) Only the minimum and maximum value of each of lists: {list3}')
    else:
        print('Items in lists must be positive!')
except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')

