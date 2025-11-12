# TODO: Write out calculation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add calculator functions to a dictionary
calculator_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use dictionary operations to multipy 4 * 8
# print(calculator_functions["*"](4, 8))

from art import logo

# re-usable calculator function
def my_calculator(num1 = None):
    print(logo)

    if num1 is None:
        num1 = float(input("What is the first number?: "))

    operation = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    answer = calculator_functions[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    return answer


# main loop
num1 = None
while True:
    answer = my_calculator(num1)

    continue_calc = input(f"Type 'y' to continue calculating with {answer}, "
                          f"type 'n' to start a new calculation, "
                          f"or type 'x' to exit: ").lower()

    if continue_calc == 'y':
        num1 = answer
    elif continue_calc == 'n':
        num1 = None
    elif continue_calc == 'x':
        break
