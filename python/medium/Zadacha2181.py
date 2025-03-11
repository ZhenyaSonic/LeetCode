"""
Вам дан headсвязанный список, содержащий ряд целых чисел, разделенных ' 0s. Начало и конец связанного списка будут иметь Node.val == 0.

Для каждых двух последовательных 0's объединить все узлы, лежащие между ними, в один узел, значение которого является суммой всех объединенных узлов. Измененный список не должен содержать никаких 0's.

Возврат измененного head связанного списка .
"""


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        ans = ListNode(0)
        tail = ans
        summa = 0
        while current:
            if current.val == 0:
                if summa > 0:
                    tail.next = ListNode(summa)
                    tail = tail.next
                summa = 0
            else:
                summa +=current.val
            current = current.next
        return ans.next
