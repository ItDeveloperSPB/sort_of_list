"""Сортировка вставкой имеет сложность O(n2)"""
from decorator import decorator_time


@decorator_time  # декоратор для замера времени
def sort_insertion(numbers: list) -> list:
    for i in range(1, len(numbers)):
        index = numbers[i]
        n = i - 1
        while numbers[n] > index and n >= 0:
            numbers[n + 1] = numbers[n]  # делаем перестановку
            n -= 1
        numbers[n + 1] = index  # устанавливаем значение

    return numbers


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
response = sort_insertion(list_of_number)  # передаем список объектов в метод
print(response)  # выводим результат
