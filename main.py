start = int(input('Start: '))
end = int(input('End: '))
if start > end:
        start, end = end, start
for i in range(start, end + 1):
    if i % 1 == 0 and i % i == 0:
        print(f'Prime numbers: {i}')