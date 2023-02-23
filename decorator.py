from time import time

def decorator_time(func):
    """ Выводит время, затраченное на выполнение переданной функции."""

    def wrapper(*args, **kwargs):
        """ Обёртка. """

        start = time()  # начинаем замер времени
        result_func = func(*args, **kwargs)  # вызываем функцию обвернутую декоратором
        end = time()  # заканчиваем замер времени
        print(f'Время выполнения функции {func.__name__}: {end - start} секунд.', end='\n\n')  #выводим информацию в поток вывода
        return result_func

    return wrapper
