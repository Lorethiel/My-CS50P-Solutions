def main():
    userinput = input('what time it is?')
    float_input = convert(userinput)
    if 7.0 <= float_input <= 8.0:
        print('breakfast time')
    elif 12.0 <= float_input <= 13.0:
        print('lunch time')
    elif 18.0 <= float_input <= 19.0:
        print('dinner time')
    else:
        quit()



def convert(time):
    hours, minutes = time.split(':')
    float_minutes_to_hours = float(minutes)/60
    float_hours = float(hours)
    time = float_hours + float_minutes_to_hours
    return float(time)

if __name__ == "__main__":
    main()