number = int(input('Number->'))
digit_3 = number % 10
number = number // 10
digit_2 = number % 10
digit_1 = number // 10
print(digit_1)
print(digit_2)
print(digit_3)
print(int(digit_1 + digit_2 + digit_3))