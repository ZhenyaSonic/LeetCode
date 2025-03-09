"""
Задан заголовок связанного списка head, в котором каждый узел содержит целое значение.

Между каждой парой соседних узлов вставьте новый узел со значением, равным их наибольшему общему делителю.

Верните связанный список после вставки.

Наибольший общий делитель двух чисел - это наибольшее натуральное число, которое делит оба числа поровну.
"""


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head

        while current and current.next:
            gcd_value = self.gcd(current.val, current.next.val)
            new_node = ListNode(gcd_value)

            new_node.next = current.next
            current.next = new_node

            current = current.next.next
        return head

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
