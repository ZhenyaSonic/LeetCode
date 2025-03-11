"""
Вам дан целочисленный массив с индексом 0nums и целое число pivot. Переставьте numsтак, чтобы были выполнены следующие условия:

Каждый элемент меньше, чем pivotпоявляется перед каждым элементом больше, чем pivot.
Каждый элемент, равный , pivotнаходится между элементами меньше и больше pivot.
Относительный порядок элементов меньше pivotи элементов больше pivotсохраняется.
Более формально, рассмотрим каждый , где — новая позиция элемента , а — новая позиция элемента . Если и оба элемента меньше ( или больше ), чем , то .pipjpiithpjjthi < jpivotpi < pj
"""


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        one = []
        two = []
        three = []
        for i in (nums):
            if i > pivot:
                one.append(i)
            elif i == pivot:
                two.append(i)
            else:
                three.append(i)
        return three+two+one
