"""Сортировка шейкерная имеет сложность O(n2)"""
from decorator import decorator_time


@decorator_time  # декоратор для замера времени
def sort_shaker(array: list) -> list:
    """сортировка коктелем"""
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right, +1):  # выполняем первый проход
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  # делаем перестановку
        right -= 1
        for i in range(right, left, -1):  # выполняем второй проход
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]  # делаем перестановку
        left += 1
    return array


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
response = sort_shaker(list_of_number)  # передаем список объектов в метод
print(response)  # выводим результат


