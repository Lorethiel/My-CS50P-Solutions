import re
import sys
import datetime
import inflect


current_date = (datetime.date.today())
cyear = current_date.year
cmonth = current_date.month
cday = current_date.day
p = inflect.engine()



def main():
    userInput = input('Date of Birth:' )
    validated_input = validate_date(userInput)
    processed_input = process_date(validated_input)
    converted_input = convert(processed_input)
    print(converted_input)







def validate_date(user_input):
    pattern = r'^([0-9]{4})-([0-9]{2})-([0-9]{2})$'
    match = re.match(pattern, user_input)
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))

        if year < 2024 and 1 <= month <= 12 and 1 <= day <= 31:
            formatted_month = str(month).zfill(2)
            formatted_day = str(day).zfill(2)
            return f'{year}-{formatted_month}-{formatted_day}'
    else:
        sys.exit(1)


def process_date(date, comparison_date=None):
    if date is not None:
        date_object = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        if comparison_date is None:
            comparison_date = datetime.date.today()

        date_difference = comparison_date - date_object
        days_difference = date_difference.days
        minute_difference = round(days_difference * 24 * 60)
        return minute_difference
    else:
        sys.exit(1)


def convert(input):
    try:
        seasons = p.number_to_words(input).replace(" and ", " ").capitalize()
        return f'{seasons} minutes'
    except:
        sys.exit(1)








if __name__ == "__main__":
    main()