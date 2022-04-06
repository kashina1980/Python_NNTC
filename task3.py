"""Написать функцию `is_empty(value)` – Если `value` пустая – вернуть `True`,
в противном случае – исходное значение"""


def is_empty(value=''):
    if not value:
        rez = True
    else:
        rez = value
    return rez


print(is_empty())
print(is_empty('abc'))
