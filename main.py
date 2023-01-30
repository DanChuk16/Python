try:
    text = input('Text: ')
    counter = 0

    lineList = text.split('.')
    newText = ''
    for val in lineList:
        val = val.strip()
        newText += val.capitalize()+'. '
    newText = newText[:-2]
    print(newText)

    for j in text:
        if j.isdigit():
            counter += 1
    print(f'Number of text: {counter}')
    number = text.count('.') + text.count('!') + text.count('?') + text.count(',') + text.count(':') + text.count(';')
    print(f'Number of offers: {number}')
    sign = text.count('!')
    print(f'The number of exclamation marks in the text: {sign}')

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')