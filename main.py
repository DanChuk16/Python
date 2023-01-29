try:
    num = input('Numbers: ').split()
    Sum = 0
    for i in num:
        Sum += i
    print(Sum)

except Exception as ex:
    print(f'Error: {ex}')