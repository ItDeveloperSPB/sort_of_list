import random
from time import time

from sort_bubble import sort_bubble
from sort_comb import sort_comb
from sort_insertion import sort_insertion
from sort_merge import merge_sort
from sort_pyramid import heap_sort
from sort_quick import sort_quick
from sort_selection import sort_selection
from sort_shaker import sort_shaker
from sort_shell import sort_shell

list_of_sorted = [sort_bubble,
                  sort_shaker,
                  sort_insertion,
                  sort_selection,
                  heap_sort,
                  sort_shell,
                  # sort_quick,
                  sort_comb,
                  merge_sort,
                  ]

list_of_number = [random.randint(0, 1000) for i in range(6000)]
for _sort in list_of_sorted:
    try:
        for _ in range(5):
            _sort(list_of_number.copy())
        print('*' * 100)
    except Exception as f:
        pass

for _ in range(5):
    new_list = list_of_number.copy()
    start = time()
    sort_quick(new_list)
    end = time()
    print(f'Время выполнения функции sort_quick : {end - start} секунд.', end='\n\n')

print('*' * 100)
for _ in range(5):
    new_list_second = list_of_number.copy()
    start = time()
    sorted(new_list_second)
    end = time()
    print(f'Время выполнения функции sorted: {end - start} секунд.', end='\n\n')

