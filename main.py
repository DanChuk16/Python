try:
    number = input('Number: ')
    filtered_number = ''.join([c for c in number if c != '3' and c != '6'])
    print(filtered_number)
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')