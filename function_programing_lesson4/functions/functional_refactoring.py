def calculate(a, b, action):
    if action == "+":
        print(a + b)
    elif action == "-":
        print(a - b)
    elif action == "/":
        print(a / b)
    else:
        print(a * b)


while True:

    calculate(
        int(input("Input number a: ")),
        int(input("Input number b: ")),
        input("Input action [+, -, /, *]: ")
    )

    print("Done!")
