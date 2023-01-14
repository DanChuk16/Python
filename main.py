try:
    text = input('Text: ')
    words = input('Reserved words: ')
    txt = text.split()
    wrds = words.split()
    for i in txt:
        if i.lower() in wrds:
            text = text.replace(i, i.upper())
    print(text)

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')