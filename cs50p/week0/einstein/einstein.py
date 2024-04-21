def main():
    m = input("m: ")
    m = int(m)

    einstein(m)


def einstein(m):
    c = 300000000
    e = m * c**2
    print("E: ", e)


main()
