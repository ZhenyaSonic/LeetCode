"""
Вам задано неотрицательное число с плавающей запятой, округленное до двух знаков после запятой по Цельсию, которое обозначает температуру в градусах Цельсия.

Вам следует преобразовать градусы Цельсия в градусы Кельвина и Фаренгейта и вернуть его в виде массива ans = [кельвин, Фаренгейт].

Верните массив ans. Будут приняты ответы в пределах 10-5 от фактического ответа.
"""


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        kelvin = celsius + 273.15
        fahrenheit = (celsius * (9/5)) + 32
        ans.append(kelvin)
        ans.append(fahrenheit)
        return ans

    # Можно заменить ans.append(kelvin) ans.append(fahrenheit) return ans return [kelvin, fahrenheit]
