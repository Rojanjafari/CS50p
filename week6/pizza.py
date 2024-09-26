from tabulate import tabulate
import csv
import sys

name, extension = sys.argv[1].split('.')

if len(sys.argv) > 2 :
    sys.exit('Too many command-line arguments')

elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

else:
    if extension != 'csv':
        sys.exit('Not a CSV file ')
    else:
        try:
            file_name = sys.argv[1]
            menu = open(file_name)
            reader = csv.DictReader(menu)
            print(tabulate(reader, headers="keys", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit('File does not exist')