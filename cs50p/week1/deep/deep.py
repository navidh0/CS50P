ans = (
    input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything?"
    )
    .lower()
    .strip()
)

match ans:
    case "42" | "forty-two" | "forty two":
        print("yes")
    case _:
        print("no")
