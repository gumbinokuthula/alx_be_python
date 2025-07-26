def perform_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        else:
            return num1 / num2
    else:
        return "Error: Unsupported operation."

print(perform_operation(10, 5, '+'))  
print(perform_operation(10, 5, '-'))  
print(perform_operation(10, 5, '*')) 
print(perform_operation(10, 0, '/')) 
print(perform_operation(10, 5, '/'))  
print(perform_operation(10, 5, '^')) 
