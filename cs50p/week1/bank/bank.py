greeting = input("Greeting: ").lower().strip()
first_char = greeting[0]

if "hello" in greeting:
    print("$0")

elif "h" == first_char:
    print("$20")

else:
    print("$100")
