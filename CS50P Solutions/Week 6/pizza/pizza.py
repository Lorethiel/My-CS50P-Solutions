import sys
import csv
from tabulate import tabulate
menu = []

def main():
    with open(get_input(sys.argv)) as file:
        values = get_values(file)
        table = get_table(values)
        print(table)




def get_input(x):

    if len(x) < 2:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(x) > 2:
        print('Too many command-line arguments')
        sys.exit(1)

    try:
        if not x[1].endswith('.csv'):
            print('Not a CSV file')
            sys.exit(1)
        return x[1]
    except FileNotFoundError:
        print('File does not exist')
        sys.exit(1)
    except IndexError:
        print('Too few command-line arguments')
        sys.exit(1)


def get_values(y):
    reader = csv.reader(y)
    for item,small,large in reader:
        menu.append({'item': item, 'small': small, 'large': large})

    return menu


def get_table(z):
    z = tabulate(z,headers='firstrow',tablefmt='grid')
    return z


if __name__ == '__main__':
    main()



