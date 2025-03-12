"""
Для заданного массива целых чисел numsвернуть количество хороших пар .

Пара (i, j)называется хорошей, если nums[i] == nums[j]и i< j.
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] in pairs:
                count += pairs[nums[i]]
            pairs[nums[i]] = pairs.get(nums[i], 0) + 1
        return count
