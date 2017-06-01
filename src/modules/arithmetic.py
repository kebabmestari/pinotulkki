def plus_handler(a, b):
    (a, b) = convert_arguments(a, b)
    return a + b


def minus_handler(a, b):
    (a, b) = convert_arguments(a, b)
    return a - b


def multiply_handler(a, b):
    (a, b) = convert_arguments(a, b)
    return a * b


def division_handler(a, b):
    (a, b) = convert_arguments(a, b)
    return a / b


# Convert arguments to integers
def convert_arguments(*args):
    return [int(i) for i in args]
