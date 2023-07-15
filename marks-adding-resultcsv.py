# IN this code a result.csv file will be generated to contain the final result instead of printing the result in the terminal

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

# Store the result in a new CSV file
output_file = 'result.csv'
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Roll Number', 'Total Marks'])  # Write header row

    for roll_number, total_marks in result.items():
        writer.writerow([roll_number, total_marks])

print(f"Result stored in '{output_file}'.")
