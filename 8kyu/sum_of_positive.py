# https://www.codewars.com/kata/5715eaedb436cf5606000381

def positive_sum(arr):
    arr_2 = []
    for x in arr:
        if x > 0:
            arr_2.append(x)
    return sum(arr_2)


test_arr = [1, 2, 3, 4]
test_arr_2 = [-1, 2, 3, 4]
test_arr_3 = []
test_arr_4 = [1]
test_arr_5 = [-1, -2, -3, -4]

print(positive_sum(test_arr))
print(positive_sum(test_arr_2))
print(positive_sum(test_arr_3))
print(positive_sum(test_arr_4))
print(positive_sum(test_arr_5))


# буквально 3 человека как я решили! остальные варианты просто космос))
# best practice:

# def positive_sum(arr):
#     return sum(x for x in arr if x > 0)
#
# def positive_sum(arr):
#     sum = 0
#     for e in arr:
#         if e > 0:
#             sum = sum + e
#     return sum
#
# def positive_sum(arr):
#     return sum(filter(lambda x: x > 0,arr))
#
# def positive_sum(arr):
#     ''' I really hate these one line codes, but here I am...
#         trying to be cool here... and writing some'''
#     return sum(map(lambda x: x if x > 0 else 0, arr))
#
# def positive_sum(arr):
#     return sum( max(i, 0) for i in arr )
#
# positive_sum = lambda a: sum(e for e in a if e > 0)
#
# def positive_sum(arr):
#     return sum([i for i in arr if i==abs(i)])