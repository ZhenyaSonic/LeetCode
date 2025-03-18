"""
Дан массив строк strs и нужно сгруппировать анаграммы вместе. Ответ можно вернуть в любом порядке.

Анаграмма — это слово или фраза, образованная путем перестановки букв другого слова или фразы, с использованием всех исходных букв ровно один раз.

Пример 1:

Ввод: strs=["ab","bat","ba","tab","ear","apt"]
Вывод:[["ab",ba"],["bat","tab"],["apt"],["ear"]]
Пример 2:

Ввод: s=["hello"]
Вывод: [["hello"]]
Ограничения:

len(strs[i]) >= 1
Строки s и t содержат только английские буквы в нижнем регистре.
"""


from typing import *
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)
    for anagram in strs: 
        count_chars = [0 for j in range(26)]
        for ch in anagram:
            count_chars[ord(ch) - ord('a')] += 1

        anagram_groups[tuple(count_chars)].append(anagram)
    return list(anagram_groups.values())
