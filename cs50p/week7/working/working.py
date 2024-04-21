import re



def main():
    print(convert(input("Hours: ")))


def convert(s):
    #p = present
    #n = next
    if matches := re.fullmatch(r'(\d{1,2}):?(\d{0,2}) (AM|PM) to (\d{1,2}):?(\d{0,2}) (AM|PM)', s):
        ph, pm, ps, nh, nm, ns = matches.groups()

        pm, nm = pm or 0, nm or 0

        ph, pm, nh, nm = map(int, [ph, pm, nh, nm])

        if ps == 'AM' and ph == 12:
            ph = 0
        elif ps == 'PM' and ph != 12:
            ph += 12

        if ns == 'AM' and nh == 12:
            nh = 0
        elif ns == 'PM' and nh != 12:
            nh += 12

        if not (0 <= ph <= 23 and 0 <= pm <= 59 and 0 <= nh <= 23 and 0 <= nm <= 59):
            raise ValueError('Invalid')

        return f'{ph:02d}:{pm:02d} to {nh:02d}:{nm:02d}'

    raise ValueError('Invalid')


if __name__ == "__main__":
    main()
