"""
Дан массив точек points. Нужно вернуть true, если существует такая прямая, параллельная оси Y, которая симметрично отражает данные точки и false, если такой прямой нет.

ВАЖНО: точки могут повторяться, но число симметричных точек не обязательно должно совпадать (см. пример 1)

Пример 1:


Ввод: points = [[1,2],[3,1],[4,2],[2,1],[2,1]]
Вывод: true
Пример 2:

Ввод: root = [[2,2],[0,0]]
Вывод: false

"""


from typing import *


def is_symmetric(points: List[List[int]]) -> bool:
    maxX = max(x for x, y in points)
    minX = min(x for x, y in points)

    points_set = {(x, y) for x, y in points}
    for x, y in points:
        if (maxX + minX - x, y) not in points_set:
            return False
    return True
