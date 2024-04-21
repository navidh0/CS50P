expression = input("Expression: ").strip().split()

x = float(expression[0])
z = expression[1]
y = float(expression[2])

match z:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x * y)
    case "/":
        print(x / y)
