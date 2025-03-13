"""
Маршрут туриста
средне
Дан набор пар городов tickets, где tickets[i] = [город отправления, город прибытия] в которых побывал турист. Нужно восстановить маршрут следования туриста.

Известно, что все города относятся к одному путешествию, и что каждый следующий перелёт турист начинал из того города, в котором закончил предыдущий и никакой город не был посещён туристом дважды.

Пример 1:

Ввод: tickets = [["Vladivostok","Moscow"]]
Вывод: ["Vladivostok","Moscow"]
Пример 2:

Ввод: tickets = [["Moscow","Yerevan"],["Vladivostok","Moscow"],["Yerevan","NY"]]
Вывод: ["Vladivostok","Moscow","Yerevan","NY"]
"""


from typing import *


def route(tickets: List[List[str]]) -> List[str]:
    # destination_cities - сет городов, куда прибывал турист
    destination_cities = set()
    # ключ: город отправления, значение: город прибытия
    mapping = {}
    for ticket in tickets:
        destination_cities.add(ticket[1])
        mapping[ticket[0]] = ticket[1]

    # ищем город из которого было отправление
    #  этот город ни разу не должен упоминяться как
    #  пункт прибытия
    start_city = ""
    for ticket in tickets:
        if ticket[0] not in destination_cities:
            start_city = ticket[0]
            break

    # начиная со start_city восстанавливаем маршрут
    result = [start_city]
    for _ in range(len(tickets)):
        result.append(mapping[result[-1]])
    return result
