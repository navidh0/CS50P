prompt = input("camelCase: ").strip()
new_string = ""
for char in prompt:
    if char.isupper():
        new_string += "_" + char
    else:
        new_string += char
new_string = new_string.lower()
print(new_string)
