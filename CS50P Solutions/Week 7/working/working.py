import re
import sys

def main():
    try:
        result = convert(input("Hours: "))
        print(result)
    except ValueError as e:
        print(f"ValueError: {e}")
        sys.exit(1)

def convert(s):
    pattern = r'(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)'
    match = re.search(pattern, s, re.IGNORECASE)

    if match:
        hour1 = int(match.group(1))
        minute1 = match.group(2)
        am_pm1 = match.group(3)
        hour2 = int(match.group(4))
        minute2 = match.group(5)
        am_pm2 = match.group(6)

        if (hour1 < 1 or hour1 > 12) or (hour2 < 1 or hour2 > 12) or (minute1 and (int(minute1) < 0 or int(minute1) > 59)) or (minute2 and (int(minute2) < 0 or int(minute2) > 59)):
            raise ValueError("Invalid time format")

        if am_pm1.lower() == 'pm' and hour1 != 12:
            hour1 += 12
        elif am_pm1.lower() == 'am' and hour1 == 12:
            hour1 = 0

        if am_pm2.lower() == 'pm' and hour2 != 12:
            hour2 += 12
        elif am_pm2.lower() == 'am' and hour2 == 12:
            hour2 = 0

        if minute1 is None:
            minute1 = '00'
        if minute2 is None:
            minute2 = '00'

        first = f'{hour1:02d}:{minute1 or "00"}'
        last = f'{hour2:02d}:{minute2 or "00"}'

        return f'{first} to {last}'

    else:
        raise ValueError

if __name__ == "__main__":
    main()
