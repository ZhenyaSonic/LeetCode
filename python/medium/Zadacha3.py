"""
Задача номер 3:
Дана строка s, найдите длину самой длинной из них. подстрокабез повторяющихся символов.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_index:
                left = max(left, char_index[s[right]] + 1)
            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length