"""Пирамидальная сортировка имеет сложность O(n * log n)"""
from decorator import decorator_time


def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — это допустимый индекс, а элемент больше,
    # чем текущий наибольший, то мы обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое и для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент уже не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


@decorator_time  # декоратор для замера времени
def heap_sort(nums: list):
    n = len(nums)

    for i in range(n, -1, -1):  # первый запуск
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в самый конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

    return nums


list_of_number = [99, 88, 77, 66, 55, 13, 2, 93]  # список объектов для сортировки
response = heap_sort(list_of_number)  # передаем список объектов в метод
print(response)  # выводим результат
