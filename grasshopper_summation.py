# https://www.codewars.com/kata/55d24f55d7dd296eb9000030

def summation(num):
    return sum(range(1, num+1))


print(summation(1))
print(summation(2))
print(summation(5))

# https://www.w3schools.com/python/ref_func_range.asp

# Syntax
# range(start, stop, step)

# Функция xrange() в Python очень похожа на функцию range() за тем лишь исключением, что вместо списка создает объект xrange.
# Производит те же элементы, что и range(), но не сохраняет их.
# Преимущества использования xrange() вместо range() заметны лишь при при работе с огромным количеством элементов или в ситуации,
# когда сами по себе созданные элементы нами не используются, нам не нужно изменять их или порядок в котором они расположены.
#
# Например, вот такая команда приведет к MemoryError
# >>> my_list = range(999999999)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# MemoryError