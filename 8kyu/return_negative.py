# https://www.codewars.com/kata/55685cd7ad70877c23000102

def make_negative(number):
    if number > 0:
        return -number
    else:
        return number

def make_negative( number ):
    return -abs(number)

print(make_negative(2))
print(make_negative(-9))
print(make_negative(0))


# best pracrice and clever

# def make_negative( number ):
#     return -abs(number)
#
# def make_negative( number ):
#     return -number if number>0 else number