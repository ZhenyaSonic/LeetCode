"""
У вас есть n боксов. Вам дана двоичная строка boxes длиной n, где boxes[i] - это "0", если i-й бокс пуст, и "1", если в нем находится один шар.

За одну операцию вы можете переместить один шар из бокса в соседний бокс. Ячейка i находится рядом с ячейкой j, если abs(i - j) == 1. Обратите внимание, что после этого в некоторых ячейках может оказаться более одного шара.

Возвращает массив answer размера n, где answer[i] - это минимальное количество операций, необходимых для перемещения всех шаров в i-ю ячейку.

Каждый ответ[i] рассчитывается с учетом начального состояния ячеек.
"""


class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        answer = [0] * len(boxes)
        for i in range(len(boxes)):
            operatons = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    operatons += abs(i-j)
            answer[i] = operatons
        return answer
