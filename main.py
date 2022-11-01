number1 = int(input('Number_1->'))
a = number1 % 10
a1 = number1 // 10
b = a1 % 10
b1 = a1 // 10
c = b1 % 10
c1 = b1 // 10
d = c1 % 10
number2 = int(d * c * b * a)
print('Number_2->', number2)