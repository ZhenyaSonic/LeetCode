"""
Учитывая целочисленный массив nums длиной n, вы хотите создать массив ans длиной 2n, где ans[i] == nums[i] и ans[i + n] == nums[i] для 0 <= i < n (с индексом 0).

В частности, ans - это объединение двух массивов nums.

Возвращает массив ans.
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i)
        return (nums+ans)

# можно вообще сделать в одну строчку return (nums+nums)
