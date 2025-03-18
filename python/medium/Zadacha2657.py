"""
Вам даны две целочисленные перестановки с индексом 0 и длиной . ABn

Префиксный общий массив и A— Bэто массив C, который C[i]равен количеству чисел, которые присутствуют в индексе или перед ним iв обоих массивах Aи B.

Верните префиксный общий массив AиB .

Последовательность nцелых чисел называется  перестановкой , если она содержит все целые числа от 1до nровно один раз.
"""


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common_array = [0] * n

    # Используем defaultdict для подсчета количества встреченных элементов
        count_map = defaultdict(int)
        common_count = 0

        for current_index in range(n):
            # Ключ здесь элемент массива, а значение - количество повторений
            count_map[A[current_index]] += 1

            # Если элемент из nums1 уже встречался в nums2, увеличиваем общий счетчик
            if count_map[A[current_index]] == 2:
                common_count += 1

            count_map[B[current_index]] += 1

            # Если элемент из nums2 уже встречался в nums1, увеличиваем общий счетчик
            if count_map[B[current_index]] == 2:
                common_count += 1

            # Сохраняем количество общих элементов на текущем индексе
            prefix_common_array[current_index] = common_count

        return prefix_common_array
