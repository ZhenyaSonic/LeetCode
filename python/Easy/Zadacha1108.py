"""
Если указан допустимый IP-адрес (IPv4) address, вернуть исправленную версию этого IP-адреса.

Очищенный IP-адрес  заменяет каждую точку "."на "[.]".
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
