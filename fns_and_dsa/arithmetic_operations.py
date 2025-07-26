def arithmetic_operations(a, b):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    tuple: A tuple containing (sum, difference, product, quotient)
    """
    if b == 0:
        quotient = "Undefined (division by zero)"
    else:
        quotient = a / b

    return (a + b, a - b, a * b, quotient)
if __name__ == "__main__":
    result = arithmetic_operations(10, 2)
    print("Sum:", result[0])
    print("Difference:", result[1])
    print("Product:", result[2])
    print("Quotient:", result[3])
