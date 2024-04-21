from sys import exit, argv
import csv


def main():
    before_file, after_file = fileCheck(argv)
    formatCheck(before_file, after_file)
    lastname, firstname, house = reader(before_file)
    writer(after_file, lastname, firstname, house)


def fileCheck(arg):
    if len(arg) != 3:
        if len(arg) > 3:
            exit("Too many command-line arguments")

        elif len(arg) < 3:
            exit("Too few command-line arguments")
    return [arg[1], arg[2]]


def reader(before):
    lastname = []
    firstname = []
    house = []
    try:
        with open(before,'r') as b_file:
             for row in csv.DictReader(b_file):
                  last, first = row["name"].split(',')
                  lastname.append(last.strip())
                  firstname.append(first.strip())
                  house.append(row['house'])
        return lastname, firstname, house

    except FileNotFoundError:
        exit("File does not exist")


def writer(after, lastname, firstname, house):
    with open(after, 'w') as a_file:
         fieldsname = ['first', 'last', 'house']
         write = csv.DictWriter(a_file, fieldnames=fieldsname)
         write.writeheader()
         for i in range(len(firstname)):
              write.writerow({'first': firstname[i], 'last': lastname[i], 'house': house[i]})


def formatCheck(first_file, second_file):
    dot1 = first_file.find('.')
    dot2 = second_file.find('.')
    if first_file[dot1:] != '.csv':
        exit("Not a CSV file")
    elif second_file[dot2:] != '.csv':
        exit("Not a CSV file")


if __name__=='__main__':
     main()

