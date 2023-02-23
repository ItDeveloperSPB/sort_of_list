"""Сортировка расческой имеет сложность O(n2)"""
from decorator import decorator_time


@decorator_time  # декоратор для замера времени
def sort_comb(numbers):
    i = int(len(numbers) / 1.247)  # устанавливаем значение
    switch = 1
    while i > 1 or switch > 0:
        switch = 0
        j = 0
        while j + i < len(numbers):
            if numbers[j] > numbers[j + i]:
                numbers[j], numbers[j + i] = numbers[j + i], numbers[i]  # делаем перестановку
                switch += 1
            j += 1
        if i > 1:
            i = int(i / 1.247)  # вышли из второго цикла и делаем проверку


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
sort_comb(list_of_number)  # передаем список объектов в метод
print(list_of_number)  # выводим результат

