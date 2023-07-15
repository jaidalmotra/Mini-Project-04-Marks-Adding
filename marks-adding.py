import csv

def calculate_total_marks(csv_file):
    total_marks = {}

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for roll_number, marks in reader:
            total_marks[roll_number] = total_marks.get(roll_number, 0) + int(marks)

    return total_marks

csv_file = 'venv/Mini Project - Marks Adding.csv'
result = calculate_total_marks(csv_file)

for roll_number, total_marks in result.items():
    print(f'Roll Number: {roll_number}, Total Marks: {total_marks}')