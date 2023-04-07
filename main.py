def calculator():
    num1 = float(input("Kérem az első számot: "))
    num2 = float(input("Kérem a második számot: "))
    op = input("Válasszon egy műveletet (+, -, *, /): ")

    if op == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif op == "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Hibás műveleti jel!")


calculator()  # Számológép indítása
