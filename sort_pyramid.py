"""Пирамидальная сортировка имеет сложность O(n)"""
from decorator import decorator_time


def heapify(array: list, size: int, index: int) -> None:
    largest = index
    left = (2 * size) + 1
    right = 2 * size + 2

    if left < size and array[index] < array[left]:
        largest = left
    if right < index and array[largest] < array[right]:
        largest = right

    if largest != index:
        array[index], array[largest] = array[largest], array[index]  # делаем перестановку
        heapify(array, size, largest)  # используем рекурсию


@decorator_time  # декоратор для замера времени
def heap_sort(nums: list) -> list:
    n = len(nums)
    for i in range(n // 2, -1, -1):  # выполняем первый запуск
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):  # выполняем второй запуск
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
heap_sort(list_of_number)  # передаем список объектов в метод
print(list_of_number)  # выводим результат

