"""Быстрая сортировка имеет сложность O(n)"""
import random
from time import time

from decorator import decorator_time


# декоратор для замера времени
# @decorator_time
def sort_quick(numbers: list) -> list:
    if len(numbers) > 1:
        j = numbers[random.randint(0, len(numbers) - 1)]  # для разделения на малые и большие
        low = [i for i in numbers if i < j]
        eq = [i for i in numbers if i == j]
        hi = [i for i in numbers if i > j]
        return sort_quick(low) + eq + sort_quick(hi)
    return numbers


list_of_numbe1r = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки

start = time()  # начинаем замер времени
test = sort_quick(list_of_numbe1r)  # передаем список объектов в метод
end = time()  # заканчиваем замер времени
print(f'Время выполнения функции {end - start} секунд.',
      end='\n\n')  # выводим информацию в поток вывода
print(test)  # выводим результат


# @decorator_time
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     return quick_sort(left) + middle + quick_sort(right)
#
# list_of_number2 = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
# start = time()  # начинаем замер времени
#
# sorted_arr = quick_sort(list_of_number2)  # передаем список объектов в метод
#
# end = time()  # заканчиваем замер времени
# print(f'Время выполнения функции {end - start} секунд.',
#       end='\n\n')  # выводим информацию в поток вывода
# print(sorted_arr)  # выводим результат
