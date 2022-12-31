def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cant be 0")
    
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)

result = calculate(10 , 30, operator=divide)