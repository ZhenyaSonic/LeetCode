"""
Напишите функцию, которая найдет самую длинную строку с общим префиксом среди массива строк.Если общего префикса нет, верните пустую строку ""
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        base = strs[0]

        for i in range(len(base)):
            for s in strs[1:]:
                if i >= len(s) or s[i] != base[i]:
                    return base[:i]
        return base
