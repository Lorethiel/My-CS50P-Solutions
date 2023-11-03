import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    n = []
    try:
        [first,second,third,last] = ip.split('.')
        n.extend([first, second, third, last])
    except ValueError:
        return False

    if len(n) != 4:
        return False


    if 255 >= int(first) >= 0 and 255 >= int(second) >= 0 and 255 >= int(third) >= 0 and 255 >= int(last) >= 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
