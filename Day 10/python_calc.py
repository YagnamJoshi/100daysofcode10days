from art import logo
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operations= {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

new_calculation='n'
while True:
    if new_calculation!='y':
        print("\n"*20)
        print(logo)
        n1 = float(input('What is your first number?: '))
    for key in operations:
        print(key)
    op = input('Pick an operation: ')
    n2 = float(input('What is the next number?: '))
    result = operations[op](n1,n2)
    print(f"{n1} {op} {n2} = {result}")
    new_calculation=input(f"Type 'y to continue calculating with {result}, or type 'n' to start a new calculation: ")
    n1 = result