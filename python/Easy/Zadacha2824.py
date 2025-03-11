"""
Дан целочисленный массив с индексом 0nums длины nи целое число target, вернуть количество пар (i, j) , где 0 <= i < j < n и nums[i] + nums[j] < target
"""


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        result = 0
        while left < right:
            if (nums[left] + nums[right]) < target:
                result += (right - left)
                left += 1
            else:
                right -= 1
        return result
