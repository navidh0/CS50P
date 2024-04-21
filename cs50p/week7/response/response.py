from validators import email as checker

if checker(input("What is your email address? ")) :
    print("Valid")
else:
    print("Invalid")
