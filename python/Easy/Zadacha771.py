"""
Вам даны строки, jewelsпредставляющие типы камней, которые являются драгоценностями, и stonesпредставляющие камни, которые у вас есть. Каждый символ в stones— это тип камня, который у вас есть. Вы хотите узнать, сколько из камней, которые у вас есть, также являются драгоценностями.

Буквы чувствительны к регистру, поэтому "a"считается другим типом камня, нежели "A".
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        my_set = set()
        count = 0 
        for i in jewels:
            my_set.add(i)
        for i in stones:
            if i in my_set:
                count += 1
        return count
