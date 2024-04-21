def main():
    # user input

    name = input()
    faces(name)


def faces(name):
    # replace str with emoji

    ans = name.replace(":)", "🙂").replace(":(", "🙁")

    # printing answer
    print(ans)


main()
