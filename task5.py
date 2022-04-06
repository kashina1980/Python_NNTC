"""Есть словари `old_` и `new_`, нужно получить cловарь, в котором ключи из обоих словарей.
По значениям приоритет у `new_`"""


def new_dict(old, new):
    old.update(new)
    return old


old_ = {
    'a': 1,
    'b': 2,
    'd': 5
}
new_ = {
    'b': 3,
    'c': 4
}
print(new_dict(old_, new_))
