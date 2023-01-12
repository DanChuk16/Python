start = int(input('Start: '))
end = int(input('End: '))
counter = 0
if start > end:
    start, end = end, start
for i in range(start, end + 1):
    if i % 1 == 0 and i % i == 0: #and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 9 != 0:
        print(f'Prime numbers: {i}')