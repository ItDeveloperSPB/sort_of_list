"""Сортировка слияния имеет сложность O(n2)"""
from decorator import decorator_time

def merge(numbers: list, number_slice: list, ls: int, le: int, rs: int, re: int) -> None:
    for i in range(ls, re + 1):
        number_slice[i] = numbers[i]

    left = ls
    right = rs
    for i in range(ls, re + 1):
        if left > le:
            numbers[i] = number_slice[right]  # в зависимости от значение устанавливаем значение
            right += 1
        elif right > re:
            numbers[i] = number_slice[left]  # в зависимости от значение устанавливаем значение
            left += 1
        elif number_slice[left] < numbers[right]:
            numbers[i] = number_slice[left]  # в зависимости от значение устанавливаем значение
            left += 1
        else:
            numbers[i] = number_slice[right]  # в зависимости от значение устанавливаем значение
            right += 1


@decorator_time  # декоратор для замера времени
def merge_sort(numbers: list) -> None:
    number_slice = numbers[::]  # получаем срез
    count = len(number_slice)
    i = 1
    while i < count:
        n = 0
        while n < count - i:
            merge(numbers, number_slice, n, n + i - 1, n + i, min(n + 2 * i - 1, count - 1))  # вызыв функции merge
            n += 2 * i  # на каждой итерации увеличиваем n
        i *= 2


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
merge_sort(list_of_number)  # передаем список объектов в метод
print(list_of_number)  # выводим результат
