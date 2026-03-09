print("Wlcome to Basic Calculator")
def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2
    
def multiply(n1, n2):
    return n1 * n2
    
def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot devide by zero!"
    return n1 / n2
# Point directly to the function names (no quotes)
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    number1 = float(input("What is the First Number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbols = input("Pick an operation from the list above: ")
        number2 = float(input("What is the Next Number?: "))
        # This looks up the function in the dictionary and calls it
        calculation_function = operations[operation_symbols] 
        answer = calculation_function(number1, number2)
        print(f"{number1} {operation_symbols} {number2} = {answer}")
        if input(f"Type 'Y' to continue with the Operation or Type 'N' to start new ") == "Y":
            number1 = answer
        else:
            should_continue = False
            calculator()
calculator()       








