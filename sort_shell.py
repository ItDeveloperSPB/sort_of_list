"""Сортировка Шелла имеет сложность O(n2)"""

import math
from decorator import decorator_time


@decorator_time  # декоратор для замера времени
def sort_shell(numbers: list) -> list:
    gap = len(numbers) // 2

    while gap > 0:
        for i in range(gap, len(numbers)):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap
            numbers[j] = temp
        gap //= 2

    return numbers


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
response = sort_shell(list_of_number)  # передаем список объектов в метод
print(response)  # выводим результат
