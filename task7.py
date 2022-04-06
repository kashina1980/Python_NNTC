"""Для упорядоченного списка произвольной длины произвольных численных значений вернуть первую пару значений,
сумма которых равна заданной (такая пара всегда есть)"""


def two_sum_2elements(lst, k):
    length = len(lst)
    for i in range(length - 1):
        for j in range(i, length):
            if lst[i] + lst[j] == k:
                return lst[i], lst[j]
    return None


print(two_sum_2elements([-3, 0, 3, 4, 8], 4))
print(two_sum_2elements([5, 6, 7, 9], 14))
print(two_sum_2elements([-3, 0, 1, 2, 4, 8], 5))


