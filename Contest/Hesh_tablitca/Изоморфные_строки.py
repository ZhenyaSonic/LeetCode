"""
Даны две строки s, t и нужно вернуть true если они изоморфны и false в обратном случае.

Строки s и t изоморфны, если символы в s можно заменить так, чтобы получить t.

ВАЖНО: каждый символ в строке должен быть заменен другим символом , при этом порядок символов должен сохраняться. Разные символы не могут заменяться на один и тот же, но символ может оставаться неизменным.

Пример 1:

Ввод: s = "abacoo", t = "gogbkk"
Вывод: true
Пример 2:

Ввод: s = "aa", t = "ab"
Вывод: false
Объяснение: буква "a" соответcтвует как символу "a", так и "b"
Пример 3:

Ввод: s = "ab", t = "aa"
Вывод: false
Объяснение: буква "a" соответcтвует как символу "a", так и "b"
Пример 4:

Ввод: s = "ab", t = "ab"
Вывод: true
"""


from typing import *

def is_isomorphic(s: str, t: str) -> bool:
    s_map, t_map = {}, {}
    for i in range(len(s)):

        if s[i] in s_map and s_map[s[i]] != t[i]:
            return False

        if t[i] in t_map and t_map[t[i]] != s[i]:
            return False

        s_map[s[i]] = t[i]
        t_map[t[i]] = s[i]
    return True
