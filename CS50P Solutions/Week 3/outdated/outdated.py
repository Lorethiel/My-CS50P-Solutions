ml = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input('Date: ').strip()
    try:
        if '/' in date:
            s = date.split('/')
            if len(s) == 3 and int(s[0]) <= 12 and int(s[1]) <= 31 and len(s[2]) == 4:
                print(f'{s[2]}-{s[0]:>02}-{s[1]:>02}')
                break
            elif int(s[0]) > 12:
                continue

        elif ',' in date:
            d1 = date.strip().replace(',', '')
            d = d1.split(' ')
            for month in ml:
                if month in date:
                    day, year = d[1], d[-1]

                    month_index = ml.index(month) + 1

            print(f'{year:>02}-{month_index:>02}-{day:>02}')
            if int(day) > 31:
                continue
            break


    except (ValueError, IndexError):
        continue
