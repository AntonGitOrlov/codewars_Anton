# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0

# не сам: https://stackoverflow.com/questions/3085382/how-can-i-strip-first-and-last-double-quotes

def remove_char(s):
    return s[1:-1]

print(remove_char('vandas'))
print(remove_char('va'))
print(remove_char('v'))
print(remove_char('vur'))