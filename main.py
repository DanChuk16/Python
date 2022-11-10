try:
    seconds = int(input('Seconds: '))
    remainder = int(86400 - seconds)
    print('#-------------------------->MENU<--------------------------#')
    print('|   hour : Show how much hours are left until midnight     |')
    print('|    min : Show how many minutes are left until midnight   |')
    print('|    sec : Show how many seconds are left until midnight   |')
    print('#----------------------------------------------------------#')
    action = input('Action: ')
    if action == 'hour':
        hours = int(remainder / 3600)
        print(f'until midnight left {hours} hours')
    elif action == 'min':
        minutes = int(remainder / 60)
        print(f'until midnight left {minutes} minutes')
    elif action == 'sec':
        print(f'until midnight left {remainder} seconds')
    else:
        hours1 = int(remainder / 3600)
        minutes2 = int((remainder % 3600) / 60)
        seconds3 = int((remainder % 3600) % 60)
        print(f'until midnight left {hours1} hours, {minutes2} minutes, {seconds3} seconds')
except:
    print('You entered something incorrectly')