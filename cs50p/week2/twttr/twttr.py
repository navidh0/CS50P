prompt = input("input: ")
vowels = ['A','E','I','O','U','a','e','i','o','u']
new_string = ""
for char in prompt:
    if char not in vowels:
        new_string += char


print(f"output: {new_string}")

