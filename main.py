try:
    string = input('String: ')
    word = input('Word to search for: ')
    word_2 = input('Replacement word: ')
    x = string.replace(word, word_2)
    print(x)

except Exception as ex:
    print(f'Error: [{ex.__class__.__name__}]: {ex}')