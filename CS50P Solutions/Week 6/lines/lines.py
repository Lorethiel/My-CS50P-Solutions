import sys

def main():
    if len(sys.argv) < 2:
        print('Too few command-line arguments')
        sys.exit(1)
    if len(sys.argv) > 2:
        print('Too many command-line arguments')
        sys.exit(1)
    if not sys.argv[1].endswith('.py'):
        print('Not a Python File')
        sys.exit(1)

    try:
        user_input = sys.argv[1]

        print(lines(user_input))

    except FileNotFoundError:
        print('File does not exist')
        sys.exit(1)


def lines(filename):
    count = 0
    with open(filename) as file:


        for line in file:
            cleaned_line = line.strip()
            if cleaned_line and not cleaned_line.startswith('#'):
                count +=1
    return count


main()






