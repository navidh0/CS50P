import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        score += check(x, y)
    print('Score:', score)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


def check(i, j):
    errors = 0
    while errors < 3:
        try:
            errors += 1
            ans = int(input(f'{i} + {j} = '))
            if ans == i + j:
                return 1
            else:
                print('EEE')
        except ValueError:
            pass
    print(f'{i} + {j} = {i+j}')
    return 0


if __name__ == "__main__":
    main()
