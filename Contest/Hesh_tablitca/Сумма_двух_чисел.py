"""
Дан массив целых чисел nums и число target. Нужно вернуть индексы двух чисел из массива nums, которые дают в сумме target.

ВАЖНО: гарантировано есть только один ответ, при этом индексы нужно вернуть в возрастающем порядке.

Пример 1:

Ввод: nums = [1,4,3,-6,2,5], target = -1
Вывод: [3,5]
Объяснение: -6 + 5 = -1. "-6" имеет индекс 3, а "5" индекс 5.
Пример 2:

Ввод: root = [4,6,4], target = 8
Вывод: [0,2]
Объяснение: дублировать число нельзя, поэтому ответы [0,0] и [2,2] не подходят.
"""


from typing import *


def two_sum(nums: List[int], target: int) -> List[int]:
    used_nums = {}
    for index, char in enumerate(nums):
        first = target - char
        if first in used_nums:
            return [used_nums[first], index]
        used_nums[char] = index
    return []
