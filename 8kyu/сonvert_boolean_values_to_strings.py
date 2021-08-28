# https://www.codewars.com/kata/53369039d7ab3ac506000467

def bool_to_word(boolean):
    # if boolean == True:
    #     return 'Yes'
    # else:
    #     return 'No'
    return 'Yes' if boolean == True else 'No'


print(bool_to_word(True))
print(bool_to_word(False))

# Best practice:

# def bool_to_word(bool):
#     return ['No', 'Yes'][bool]
#
# bool_to_word = {True: 'Yes', False: 'No'}.get
#
# bool_to_word = ['No','Yes'].__getitem__
#
# bool_to_word = lambda b: b and "Yes" or "No"