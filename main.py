# Є цілі числа h , m:
# h(0 < h <= 12)
# m(0 <= m <= 59)
# Формат "h годин, m хвилин"
# Знайти найменшу кількість повних хвилин, які повинні пройти до моменту, коли годинна і хвилина стрілка на циферблаті:
# а) співпадають
# б) розполягаються перпендикулярно один одному
try:
    while True:
        h = int(input('Hour: '))
        if h >= 13 or h <= 0:
            print('Error: A number greater than 12 or less than 1. Repeat, please:')
        else:
            break

    while True:
        m = int(input('Minutes: '))
        if m >= 60 or m <= -1:
            print('Error: A number greater than 59 or less than 0. Repeat, please:')
        else:
            break

    h_to_m = int(h * 5)
    match = int(h_to_m - m)
    if match < 0:
        match = match + 60
    if match > 12 and match <= 24:
        match = match + 1
    elif match > 24 and match <= 36:
        match = match + 2
    elif match > 36 and match <= 48:
        match = match + 3
    elif match > 48 and match <= 59:
        match = match + 4
    print(f'a) Match by: {match}')

    match = int(h_to_m - m)
    perp = 0
    if h_to_m > m:
        if match < 15:
            perp = match + 15
        elif match < 30 and match > 15:
            perp = match - 15
        elif match < 45 and match > 30:
            perp = match - 15
        elif match < 60 and match > 45:
            perp = match - 45
    elif h_to_m < m:
        match = int(m - h_to_m)
        if match < 15:
            perp = 15 - match
        elif match < 30 and match > 15:
            perp = match - 5
        elif match < 45 and match > 30:
            perp = match - 30
        elif match < 60 and match > 45:
            perp = match - 45

    print(f'b) Perpendicular to each other by: {perp}')

except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')