try:
    seconds = int(input('Seconds: '))
    remainder = int(86400 - seconds)
    print('#------------------------->MENU<-------------------------#')
    print('|   h : Show how much hours are left until midnight      |')
    print('|   m : Show how many minutes are left until midnight    |')
    print('|   s : Show how many seconds are left until midnight    |')
    print('#--------------------------------------------------------#')
    action = input('Action: ')
    if action == 'h':
        hours = int(remainder / 3600)
        print(f'until midnight left {hours} hours')
    elif action == 'm':
        minutes = int(remainder / 60)
        print(f'until midnight left {minutes} minutes')
    elif action == 's':
        print(f'until midnight left {remainder} seconds')
    else:
        hours1 = int(remainder / 3600)
        minutes2 = int((remainder % 3600) / 60)
        seconds3 = int((remainder % 3600) % 60)
        print(f'until midnight left {hours1}:{minutes2}:{seconds3}')
except:
    print('     !!!ERROR!!!     \nYou entered something incorrectly!')