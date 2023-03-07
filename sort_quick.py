"""Быстрая сортировка имеет сложность O(n logn)"""
from time import time


def sort_quick(numbers: list) -> list:
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]

    return sort_quick(left) + middle + sort_quick(right)


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки

start = time()  # начинаем замер времени
response = sort_quick(list_of_number)  # передаем список объектов в метод
end = time()  # заканчиваем замер времени
print(f'Время выполнения функции {end - start} секунд.', end='\n\n')  # выводим информацию в поток вывода
print(response)  # выводим результат
