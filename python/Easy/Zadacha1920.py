"""Для заданной перестановки, начинающейся с нуля nums ( индексированной с 0 ), создайте массив ansтой же длины , где ans[i] = nums[nums[i]]для каждого элемента 0 <= i < nums.length, и верните его.

Перестановка с нулевой базой nums — это массив различных целых чисел от 0до nums.length - 1( включительно ).
Решение:
"""


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            ans[i] = nums[nums[i]]
        return ans
