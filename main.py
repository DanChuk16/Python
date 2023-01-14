try:
    text = input('Text: ')
    number = text.count('.') + text.count('!') + text.count('?')
    print(f'Number of offers: {number}')

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')