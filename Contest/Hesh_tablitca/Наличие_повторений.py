"""
Дан массив целых чисел nums, верни true, если любое значение встречается хотя бы два раза, и верни false, если все элементы уникальны.

Пример 1:

Ввод: nums = [1,4,3,1]
Вывод: true
Объяснение: элемент со значением 1 встречается два раза в 0 и 3 индексе.
Пример 2:

Ввод: nums = [1,2,3,4]
Вывод: false
Объяснение: все элементы уникальны.
"""


from typing import *


def contains_duplicate(nums: List[int]) -> bool:
    used = dict()
    for num in nums:
        if num in used:
            return True
        used[num] = True
    return False
