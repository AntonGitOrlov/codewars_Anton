def close_compare(a, b, margin=0):
    if a > b and not margin >= a - b:
        return 1
    elif a < b and not margin >= a - b:
        return -1
    else:
        return 0

var_1 = close_compare(10, 4, 1)
print(var_1)
