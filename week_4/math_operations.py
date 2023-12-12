def basic_operations(a, b):
    try:
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b
        return {
            'addition': addition,
            'subtraction': subtraction,
            'multiplication': multiplication,
            'division': division
        }
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input.")

def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            modulo = kwargs['modulo']
            result %= modulo
        return result
    except TypeError:
        print("Error: Invalid input.")

def apply_operations(operation_list):
    try:
        results = list(map(lambda x: x[0](*x[1]), operation_list))
        return results
    except TypeError:
        print("Error: Invalid input.")