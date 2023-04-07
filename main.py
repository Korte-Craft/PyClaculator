def calculator():
    num1 = float(input("First number: "))
    num2 = float(input("Secund number: "))
    op = input("(+, -, *, /): ")

    if op == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif op == "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error")


calculator()  # Számológép indítása
