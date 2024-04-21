def main():
    prompt = input("input: ")
    print('Output:', shorten(prompt))

def shorten(word):
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    new_string = ""
    for char in word:
        if char not in vowels:
            new_string += char
    return f'{new_string}'

if __name__ == "__main__":
    main()
