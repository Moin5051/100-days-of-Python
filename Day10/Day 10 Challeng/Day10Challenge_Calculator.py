from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def div(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2

Calc = {
    "+" : add,
    "-": sub,
    "*": multiply,
    "/": div
}

def calculator():
    first_number = float(input("What is the first Number? : "))
    repeating = True
    while repeating:


        operator = input(f"Choose an operator: \n + \n - \n * \n / \n : ")
        second_number = float(input("What is the last number? : "))

        ans = Calc[operator](first_number, second_number)
        print(f"{first_number}{operator}{second_number} = {ans}")
        rep = input(f"Would you like to continue with {ans}? Press Y for yes and N to enter new numbers: ").lower()

        if rep == "y":
            first_number = ans
        else:
            repeating = False
            print("\n" * 100)
            calculator()


calculator()