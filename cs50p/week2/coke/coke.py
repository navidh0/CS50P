price = int(50)
due = price
while due > 0:
    print (f"Amount Due: {due}")
    change = int(input("insert coin: "))
    if change == 25 or change == 10 or change == 5:
        due -= change

if due < 0:
    due = -due

print(f"Change Owed: {due}")


