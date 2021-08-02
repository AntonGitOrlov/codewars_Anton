# https://www.codewars.com/kata/5715eaedb436cf5606000381

def positive_sum(arr=[0]):
    for x in arr:
        return sum(arr)
        # if x > 0:
        #     return sum(arr)
        # elif x == []:
        #     return 0
        # else:
        #     return 0


test_arr = [1, 2, 3, 4]
test_arr_2 = [-1, 2, 3, 4]
test_arr_3 = []
test_arr_4 = [1]

print(positive_sum(test_arr))
print(positive_sum(test_arr_2))
print(positive_sum(test_arr_3))
print(positive_sum(test_arr_4))
print(positive_sum())