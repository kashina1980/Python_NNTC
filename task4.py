"""Есть список, написать функцию `clean(list_)`, которая создаст список, в котором останутся только числа:"""


def clean(list_):
    digits = []
    for element in list_:
        if type(element) == int or type(element) == float:
            digits.append(element)
    return digits


temp_ = [1, 2, 'same_string', 3, 'other string']
print(clean(temp_))
