"""Для упорядоченного списка произвольной длины произвольных численных значений вернуть первую пару значений,
сумма которых равна заданной (такая пара всегда есть)"""


def two_sum_2elements(lst, k):
    length = len(lst)
    low = 0
    high = length
    for i in range(length):
        diff = k - lst[i]
        while low <= high:
            mid = (low + high) // 2
            if (lst[mid] == diff) and (mid != i):
                return lst[i], lst[mid]
            elif lst[mid] > diff:
                high = mid - 1
            else:
                low = mid + 1


print(two_sum_2elements([-3, 0, 3, 4, 8], 4))
print(two_sum_2elements([5, 6, 7, 9], 14))
print(two_sum_2elements([-3, 0, 1, 2, 4, 8], 5))
