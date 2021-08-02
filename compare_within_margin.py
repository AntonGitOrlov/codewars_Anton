# https://www.codewars.com/kata/56453a12fcee9a6c4700009c

def close_compare(a, b, margin=0):
    if a > b and not margin >= abs(a - b): # a is higher than b
        return 1
    elif a < b and not margin >= abs(a - b): # a lower than b
        return -1
    else: # a is close to b
        return 0

var_1 = close_compare(10, 4, 1)
print(var_1)
