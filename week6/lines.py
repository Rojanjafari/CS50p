import sys

name, extension = sys.argv[1].split('.')

if len(sys.argv) > 2 :
    sys.exit('Too many command-line arguments')

elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

else:
    if extension != 'py':
        sys.exit('Not a Python file ')
    else:
        try:
            file_name = sys.argv[1]
            file = open(file_name).read()
            lines = file.split('\n')

            num_lines = 0
            for line in lines:
                if line:
                    if line.strip().startswith('#') == False and line.strip() != "":
                        num_lines += 1

            print(num_lines)


        except FileNotFoundError:
            sys.exit('File does not exist')
