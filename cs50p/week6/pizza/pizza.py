import sys
import csv
from tabulate import tabulate


def main():
    filename = fileCheck(sys.argv)
    formatCheck(filename)
    formater(filename)


def fileCheck(arg):
    if len(sys.argv) != 2:
        if sys.argv > 2:
            sys.exit("Too many command-line arguments")

        elif sys.argv < 2:
            sys.exit("Too few command-line arguments")
    return arg[1]


def formatCheck(filename):
    dot = filename.find('.')
    if filename[dot:] != '.csv':
        sys.exit("Not a CSV file")


def formater(filename):
    try:
        with open(filename) as file:
            table = []
            header = list(next(csv.reader(file)))
            for row in csv.reader(file):
                table.append(row)

        print(tabulate(table, header, tablefmt='grid'))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
