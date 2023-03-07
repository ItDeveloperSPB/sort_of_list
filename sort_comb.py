"""Сортировка расческой имеет сложность O(n2)"""
from decorator import decorator_time


@decorator_time  # декоратор для замера времени
def sort_comb(numbers) -> list:
    i = len(numbers)  # устанавливаем значение
    shrink = 1.247
    switch = False
    while not switch:
        i = int(i/shrink)
        if i <= 1:
            i = 1
            switch = True

        j = 0
        while j + i < len(numbers):
            if numbers[j] > numbers[j + i]:
                numbers[j], numbers[j + i] = numbers[j + i], numbers[j]  # делаем перестановку
                switch = False
            j += 1

    return numbers


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
response = sort_comb(list_of_number)  # передаем список объектов в метод
print(response)  # выводим результат
