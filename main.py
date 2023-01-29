try:
    num = input('Numbers: ').split()
    someNum = input('Some number: ')
    count = 0
    for i in num:
        if someNum in i:
            count += 1
    print(f'The number {someNum} occurred {count} times. ')

except Exception as ex:
    print(f'Error: {ex}')