try:
    size = float(input('Size (Gb): '))
    speed = float(input('Speed (Bit/s): '))
    print('#------------------------------>MENU<------------------------------#')
    print('|   h : Show how many hours it will take to download the file      |')
    print('|   m : Show how many minutes it will take to download the file    |')
    print('|   s : Show how many seconds it will take to download the file    |')
    print('#------------------------------------------------------------------#')
    action = input('Action: ')
    bits = float(size * 8589934592)
    time_sec = float(bits / speed)
    if action == 'h':
        print(int(time_sec / 3600), 'hours to download the file')
        # print(f'{time_sec / 3600} hours to download the file')
    elif action == 'm':
        print(int(time_sec / 60), 'minutes to download the file')
        # print(f'{time_sec / 60} minutes to download the file')
    elif action == 's':
        print(int(time_sec), 'seconds to download the file')
        # print(f'{time_sec} seconds to download the file')
    else:
        print(int(time_sec / 3600), ':', int((time_sec % 3600) / 60), ':', int((time_sec % 3600) % 60), 'to download the file')
        #print(f'{(time_sec / 3600)}:{((time_sec % 3600) / 60)}:{(time_sec % 3600) % 60} to download the file')
except:
    print('   !!!ERROR!!!   \nYou typed something wrong!')