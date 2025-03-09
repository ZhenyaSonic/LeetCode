"""Учитывая строку s, содержащую только символы '(', ')', '{', '}', '[' и ']', определите, допустима ли входная строка.

Входная строка допустима, если:

Открытые скобки должны быть заключены в скобки того же типа.
Открытые скобки должны закрываться в правильном порядке.
Каждой закрывающейся скобке соответствует открытая скобка того же типа."""


class Solution:
    def isValid(self, s: str) -> bool:

        base = []
        dictanory = {')': '(', ']': '[', '}': '{'}

        for i in (s):
            if i in dictanory.values():
                base.append(i)
            elif i in dictanory.keys():
                if not base or dictanory[i] != base.pop():
                    return False
        return not base
