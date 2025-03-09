'''
Вам задана строка s. 
Оценка строки определяется как сумма абсолютных разностей между ASCII-значениями соседних символов.
Возвращает оценку s.
'''


class Solution:
    def scoreOfString(self, s: str) -> int:

        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score
