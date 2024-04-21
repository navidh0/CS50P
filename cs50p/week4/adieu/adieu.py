import inflect

p = inflect.engine()
names = []

while True:
    try:
        names.append(input('name: '))

    except EOFError:
        break

print(f'Adieu, adieu, to {p.join(names)}')
