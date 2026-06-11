def add_numbers(num1, num2):
    return num1 + num2


def sub_numbers(num1, num2):
    return num1 - num2


def mul_numbers(num1, num2):
    return num1 * num2


def div_numbers(num1, num2):
    return num1 / num2


def main():
    num1 = float(input("Num1: "))
    operator = input("Operator: ")
    num2 = float(input("Num2: "))

    if operator == "+":
        result = add_numbers(num1, num2)
    elif operator == "-":
        result = sub_numbers(num1, num2)
    elif operator == "*":
        result = mul_numbers(num1, num2)
    elif operator == "/":
        result = div_numbers(num1, num2)
    else:
        print("bunday operator yoq")

    print(f"{num1} {operator} {num2} = {result}")


main()

