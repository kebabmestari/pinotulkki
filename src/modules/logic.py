def and_handler(a, b):
    (a, b) = convert_arguments(a, b)
    return a and b


def or_handler(a, b):
    (a, b) = convert_arguments(a, b)
    return a or b


def not_handler(a):
    (a,) = convert_arguments(a)
    return not a


# Convert arguments to integers
def convert_arguments(*args):
    return [bool(i) for i in args]
