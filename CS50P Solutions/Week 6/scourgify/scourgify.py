import csv
import sys

def main():
    if len(sys.argv) < 3:
        print('Too few command-line arguments')
        sys.exit(1)
    if len(sys.argv) > 3:
        print('Too many command-line arguments')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith('.csv'):
        print('Input file is not a CSV file')
        sys.exit(1)

    try:
        students = get_values(input_file)
        writer(students, output_file)
    except FileNotFoundError:
        print('Input file does not exist')

def get_values(input_file):
    students = []
    try:
        with open(input_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name_parts = row["name"].strip('"').split(',')
                last, first = name_parts
                students.append({'first': first, 'last': last, 'house': row["house"]})
            return students
    except FileNotFoundError:
        sys.exit(1)

def writer(students, output_file):
    fieldnames = ['first', 'last', 'house']

    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            first_name = student['first'].strip()
            last_name = student['last'].strip()
            writer.writerow({'first': first_name, 'last': last_name, 'house': student['house']})

if __name__ == "__main__":
    main()
