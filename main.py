number_1 = int(input('Number_1 = '))
number_2 = 0
while number_1 > 0:
    digit = number_1 % 10
    number_1 = number_1 // 10
    number_2 = number_2 * 10
    number_2 = number_2 + digit
print('Number_2 =', number_2)