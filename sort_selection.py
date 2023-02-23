"""Сортировка выбором имеет сложность O(n2)"""
from decorator import decorator_time


@decorator_time  # декоратор для замера времени
def sort_selection(numbers):
    for num in range(len(numbers)):
        min_value = num
        for item in range(num, len(numbers)):
            if numbers[min_value] > numbers[item]:
                min_value = item
        numbers[num], numbers[min_value] = numbers[min_value], numbers[num]  # делаем установку значений
    return numbers


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
sort_selection(list_of_number)  # передаем список объектов в метод
print(list_of_number)  # выводим результат
