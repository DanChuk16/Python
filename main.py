try:
    begin = int(input('Begin:'))
    end = int(input('End:'))

    for item in range(begin, end + 1):
        print(item, end='\t')

except:
    print('You entered the wrong number!')