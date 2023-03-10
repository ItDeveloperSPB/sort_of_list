"""Сортировка пузырьком имеет сложность O(n2)"""
from decorator import decorator_time


@decorator_time  # декоратор для замера времени
def sort_bubble(array: list) -> list:
    switch = True
    while switch:
        switch = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  # перестановка элементов
                switch = True  # устанавливаем для следущей итерации
    return array


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
response = sort_bubble(list_of_number)  # передаем список объектов в метод
print(response)  # выводим результат
