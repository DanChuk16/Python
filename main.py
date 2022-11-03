number_1 = int(input('Number_1 = '))
number_2 = 0
while number_1 > 0:
    digit = number_1 % 10
    number_1 = number_1 // 10
    number_2 = number_2 * 10
    number_2 = number_2 + digit
print('Number_2 =', number_2)

number_1 = int(input('Number_1 = '))
a = int(number_1 % 10)
a1 = int(number_1 // 10)
b = int(a1 % 10)
b1 = int(a1 // 10)
c = int(b1 % 10)
d = int(b1 // 10)
print('Number_2 =', int((a * 1000) + (b * 100) + (c * 10) + d))