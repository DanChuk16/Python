try:
    hour = int(input('Hours: '))
    if hour >= 0 and hour < 6:
        print('Good Night')
    elif hour >= 6 and hour < 13:
        print('Good Morning')
    elif hour >= 13 and hour < 17:
        print('Good Day')
    elif hour >= 17 and hour < 24:
        print('Good Evening')
    else:
        print('Such an hour does not exist!')
except:
    print('   !!!ERROR!!!   \nYou have not entered an hour!')