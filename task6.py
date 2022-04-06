"""Есть словарь, нужно получить новый словарь в котором ключи как удвоенные `key`→ `keykey`,
а значения – удвоенные значения `x`→ `x*2`:"""


def dict_double(dict_):
    new_dict = {}
    for key in dict_:
        new_dict[key*2] = dict_[key]*2
    return new_dict


item = {
    'a': 10,
    'b': 20,
    'c': 30
}
print(dict_double(item))
