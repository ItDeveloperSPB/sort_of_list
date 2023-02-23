"""Быстрая сортировка имеет сложность O(n)"""
import random

from decorator import decorator_time


@decorator_time  # декоратор для замера времени
def sort_quick(numbers: list) -> list:
    if len(numbers) > 1:
        j = numbers[random.randint(0, len(numbers) - 1)]  # для разделения на малые и большие
        low = [i for i in numbers if i < j]
        eq = [i for i in numbers if i == j]
        hi = [i for i in numbers if i > j]
        numbers = sort_quick(low) + eq + sort_quick(hi)
    return numbers


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
sort_quick(list_of_number)  # передаем список объектов в метод
print(list_of_number)  # выводим результат
