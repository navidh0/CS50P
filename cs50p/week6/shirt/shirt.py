from sys import exit, argv
from PIL import Image, ImageOps


def main():
    before_file, after_file = fileCheck(argv)
    formatCheck(before_file, after_file)
    resizer(before_file, after_file)


def fileCheck(arg):
    if len(arg) != 3:
        if len(arg) > 3:
            exit("Too many command-line arguments")

        elif len(arg) < 3:
            exit("Too few command-line arguments")
    return arg[1], arg[2]


def formatCheck(first_file, second_file):
    dot1 = first_file.lower().find('.')
    dot2 = second_file.lower().find('.')
    if first_file[dot1:] != '.jpg' and '.jpeg' and '.png':
        exit("Invalid output")
    elif second_file[dot2:] != '.jpg' and '.jpeg' and '.png':
        exit("Invalid output")

    elif first_file[dot1:] != second_file[dot2:]:
        exit("Input and output have different extensions")


def resizer(inputFile, outputFile):
    try:
        shirt = Image.open('shirt.png')
        muppet = Image.open(inputFile)
        size = shirt.size
        muppet = ImageOps.fit(muppet, size)
        muppet.paste(shirt, shirt)
        muppet.save(outputFile)

    except FileNotFoundError:
        exit('Input does not exist')


if __name__ == '__main__':
    main()
