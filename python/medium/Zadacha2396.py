"""
Целое число nявляется строго палиндромным , если для каждого основания bот 2до n - 2( включительно ) строковое представление целого числа nв основании bявляется палиндромным .

Если задано целое число n, вернуть , true если nоно строго палиндромное, и , falseв противном случае .

Строка является палиндромной, если она одинаково читается слева направо и слева направо.
"""


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        if n == 0:
            return "0"

        binary = ""
        while n > 0:
            remainder = n % 2
            binary = str(remainder) + binary
            n = n // 2

            if binary == reversed(binary):
                return True
            else:
                return False
