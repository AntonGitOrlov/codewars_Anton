# https://www.codewars.com/kata/55a2d7ebe362935a210000b2

def find_smallest_int(arr):
    return min(arr)

print(find_smallest_int([78, 56, 232, 12, 11, 43]))
print(find_smallest_int([78, 56, -2, 12, 8, -33]))
print(find_smallest_int([0, 1-2**64, 2**64]))

# other vars:

# findSmallestInt=min
# print(findSmallestInt([78, 56, 232, 12, 11, 43]))

# def findSmallestInt(arr):
#     """
#     input: arr, a list of integers
#     output: smallest integer in arr
#     """
#
#     # check that each element is an int
#     for num in arr:
#         assert type(num) == int
#
#     # sort array
#     arr.sort()
#
#     # return smallest value
#     return arr[0]
