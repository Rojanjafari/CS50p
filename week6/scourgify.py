import sys
import csv

students = []

if len(sys.argv) > 3 :
    sys.exit('Too many command-line arguments')

elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

else:
    try:
        file_name = sys.argv[1]
        file = open(file_name)
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row['name'].split(', ')
            students.append({"first" : first, "last" : last, "house": row['house']})

        with open(sys.argv[2] , "w", newline='') as new_file:
            writer = csv.DictWriter(new_file, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for row in students:
                writer.writerow(row)

    except FileNotFoundError:
        sys.exit('Could not read invalid_file.csv')