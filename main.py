try:
    begin = int(input('Begin:'))
    end = int(input('End:'))

    for item in range(begin, end + 1):
        print(item, end='\t')

except ValueError as vl_ex:
    print(f'Value Error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')