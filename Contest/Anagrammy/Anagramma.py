"""
Даны две строки s и t, нужно вернуть true, если t является анаграммой s, и false в противном случае.

Анаграмма — это слово или фраза, образованная путем перестановки букв другого слова или фразы, с использованием всех исходных букв ровно один раз.
"""


from typing import *


def is_valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}
    for char in s:
        s_map[char] = s_map.get(char, 0) + 1

    for char in t:
        t_map[char] = t_map.get(char, 0) + 1

    return s_map == t_map

# Второе решения для ACII если будет известно число букв условно
from typing import *


def is_valid_anagram(s: str, t: str) -> bool:
    # индекс - соответствует букве (0 - 'a', 1 - 'b', ...)
    #  значение - сколько раз встретили букву
    count = [0 for _ in range(26)]
    for char in s:
        # ord(char) - ord('a') - позволяет перевести 'a' -> 0, 'b' -> 1 и т д
        count[ord(char) - ord('a')] += 1

    # уменьшаем число букв, которые встретили проходя по строке t
    #  делаем это чтобы не заводить второй массив count.
    #  Если в самом конце массив получился только из 0 - значит
    #  все буквы в строках повтаряются
    for char in t:
        count[ord(char) - ord('a')] -= 1

    return count == [0 for _ in range(26)]