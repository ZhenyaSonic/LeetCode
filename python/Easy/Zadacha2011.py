"""
Существует язык программирования, содержащий всего четыре операции и одну переменную X:

++Xи X++ увеличивает значение переменной Xна 1.
--Xи X-- уменьшает значение переменной Xна 1.
Первоначально значение Xравно 0.

Дан массив строк, содержащийoperations список операций, вернуть конечное значение X после выполнения всех операций .
"""


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        results = 0
        for i in operations:
            if i == "X++" or i == "++X":
                results += 1
            else:
                results -=1
        return results
