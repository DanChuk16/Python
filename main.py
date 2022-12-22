try:
    start = int(100)
    end = int(9999)
    counter = 0
    for i in range(start, end + 1):
        a = (i // 1000) % 10
        b = (i // 100) % 10
        c = (i // 10) % 10
        d = i % 10
        if a != b and a != c and a != d and b != c and b != d and c != d:
            counter += 1
    print(f'Start: {start}\nEnd: {end}\nIntegers that have two identical digits: {counter}')

except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')