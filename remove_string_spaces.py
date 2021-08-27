# https://www.codewars.com/kata/57eae20f5500ad98e50002c5

def no_space(string):
    list_form_string = string.split()
    return ''.join(list_form_string)

string_with_spaces = no_space('rrtg  tgtg    tgtgt tg')
print(string_with_spaces)

# vars of others (извращенцы некоторые):

# def no_space(x):
#     return x.replace(' ' ,'')

# def no_space(x):
#     return "".join(x.split())

# def no_space(x):
#     return ''.join(i for i in x if i !=' ')

# no_space = lambda s: ''.join(filter(lambda ch: not ch == ' ', s))

# import re
#
# def no_space(x):
#     return re.sub(r'\s+','',x,0)