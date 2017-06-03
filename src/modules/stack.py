# dup
# duplicates the top of the stack
def dup_handler(a):
    return [a, a]


# swap
# swaps two entries from the top of the stack
def swap_handler(a, b):
    return [a, b]


# drop
# does nothing, returns nothing -> discards the top of the stack
def drop_handler(a):
    return None


# rot
# rotates the third item to the top
def rot_handler(a, b, c):
    return [b, a, c]


# over
# pushes copy of the second item to the top
def over_handler(a, b):
    return [b, a, b]


# nip
# removes the second item
def nip_handler(a, b):
    return a


# tuck
# pushes copy of the top into third
def tuck_handler(a, b):
    return [a, b, a]
