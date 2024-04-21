import sys

if len(sys.argv) != 2:
    if sys.argv > 2:
        sys.exit("Too many command-line arguments")

    elif sys.argv < 2:
        sys.exit("Too few command-line arguments")


filename = sys.argv[1]
code_format = filename.find('.')

if filename[code_format:] != '.py':
    sys.exit("Not a Python file")


loc = 0

try:
    with open(filename) as file:
        for line in file:
            if line.isspace():
                continue
            if line.strip().startswith('#'):
                continue

            loc += 1

except FileNotFoundError:
    sys.exit("File does not exist")


print(loc)
