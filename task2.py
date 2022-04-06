"""Есть словарь, нужно получить значение по ключу `weight`, если его нет - получить 0"""


temp_ = {
    'name': 'simple',
    'weight': 5
}
key = 'weight'
if key in temp_:
    value = temp_[key]
else:
    value = 0
print(value)
