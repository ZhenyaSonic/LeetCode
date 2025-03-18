"""
Есть nлюди, которые разделены на неизвестное количество групп. Каждый человек помечен  уникальным идентификатором  от  0 до  n - 1.

Вам дан целочисленный массив  groupSizes, где groupSizes[i] — размер группы,  i в которой находится человек. Например, если  groupSizes[1] = 3, то человек  1 должен быть в группе размером  3.

Верните  список групп таким образом, чтобы каждый человек  i входил в группу размера groupSizes[i] .

Каждый человек должен быть представлен  ровно в одной группе , и каждый человек должен быть в группе. Если есть несколько ответов, верните любой из них . Гарантируется , что для данного ввода будет по крайней мере одно допустимое решение.
"""


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []
        for idx, char in enumerate(groupSizes):
            if char not in groups:
                groups[char] = []
            groups[char].append(idx)

            if len(groups[char]) == char:
                result.append(groups[char])
                groups[char] = []
        return result
