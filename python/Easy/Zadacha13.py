"""
Задача номер 13:
Римские цифры представлены семью различными символами  : I, V, X, L, и .CDM

Символ        Значение
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
Например,  2записывается как II римская цифра, просто две единицы, сложенные вместе. 12записывается как  XII, что просто X + II. Число 27записывается как XXVII, что XX + V + II.

Римские цифры обычно пишутся от большего к меньшему слева направо. Однако цифра для четырех не IIII. Вместо этого число четыре записывается как IV. Поскольку единица стоит перед пятью, мы вычитаем ее, получая четыре. Тот же принцип применим к числу девять, которое записывается как IX. Существует шесть случаев, когда используется вычитание:

Iможно поместить перед V(5) и X(10), чтобы получить 4 и 9.
Xможно поместить перед L(50) и C(100), чтобы получить 40 и 90.
Cможно разместить перед D(500) и M(1000), чтобы получить 400 и 900.
Данную римскую цифру преобразуйте в целое число.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_map[char]

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value

        return total
