"""
У вас есть массив средних значений чисел с плавающей запятой, который изначально пуст. Вам задан массив nums из n целых чисел, где n - четное число.

Вы повторяете следующую процедуру n / 2 раза:

Удалите наименьший элемент minElement и наибольший элемент maxElement из nums.
Добавьте (minElement + maxElement) / 2 к средним значениям.
Верните минимальный элемент в виде средних значений.
"""


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        average = []
        left, right = 0, len(nums) - 1
        while left < right:
            average.append((nums[left] + nums[right]) / 2)

            left += 1
            right -= 1
        return min(average)
