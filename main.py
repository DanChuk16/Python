try:
    start = int(100)
    end = int(999)
    counter = 0
    for i in range(start, end + 1):
        a = (i // 100) % 10
        b = (i // 10) % 10
        c = i % 10
        if a == b or a == c or b == c:
            counter += 1
    print(f'Start: {start}\nEnd: {end}\nIntegers that have two identical digits: {counter}')

except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')