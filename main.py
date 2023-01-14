try:
    string = input('String: ')
    string_2 = string.lower()
    str = (string_2[::-1])
    if string_2 == str:
        print(f'This is palindrome! \n{string_2} = {str}')
    else:
        print('There is no palindrome!')

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')