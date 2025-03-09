'''

Задача номер 1:
Дан массив целых чисел nums и целое число target, вернуть индексы двух чисел, чтобы их сумма давалаtarget .

Вы можете предположить, что каждый вход будет иметь ровно одно решение , и вы не можете использовать один и тот же элемент дважды.

Вы можете возвращать ответ в любом порядке.
Первое решение:
'''


class Solution:
    def twoSum(self, nums, target):
        num_to_index = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return None


"""Второе решение:"""


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
