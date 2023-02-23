"""Сортировка Шелла имеет сложность O(n2)"""

import math
from decorator import decorator_time


@decorator_time  # декоратор для замера времени
def sort_shell(numbers: list) -> list:
    num = len(numbers)
    key = int(math.log2(num))
    interval = 2 ** key - 1
    while interval > 0:
        for i in range(interval, num):
            temp = numbers[i]
            j = i
            while j >= interval and numbers[j - interval] > temp:
                numbers[j] = numbers[j - interval]  # делаем перестановку
                j -= interval
            numbers[j] = temp
        key -= 1
        interval = 2 ** key - 1  # устанавливаем значение счетчику
    return numbers


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
sort_shell(list_of_number)  # передаем список объектов в метод
print(list_of_number)  # выводим результат
