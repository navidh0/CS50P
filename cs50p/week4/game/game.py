import random

while True:
    try:
        n = int(input('Level: '))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        pass


goal = random.randint(1, n)
while True:
    try:
        prediction = int(input('Guess: '))
        if goal > prediction:
            print('Too small!')
        elif goal < prediction:
            print('Too large!')
        else:
            print('Just right!')
            break

    except ValueError:
        pass
