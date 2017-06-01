def lt_handler(a, b):
    (a, b) = convert_arguments(a, b)
    return a < b

def gt_handler(a, b):
    (a, b) = convert_arguments(a, b)
    return a > b

def eq_handler(a, b):
    (a, b) = convert_arguments(a, b)
    return a == b

def neq_handler(a, b):
    (a, b) = convert_arguments(a, b)
    return a != b

# Convert arguments to integers
def convert_arguments(*args):
    return [int(i) for i in args]