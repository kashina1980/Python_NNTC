"""Есть словарь, нужно удалить элемент `alias`, был ли он уже удалён - неизвестно:"""


item = {
    'name': 'weight',
    'value': '100',
    'alias': 'Масса'
    }
key = 'alias'
if key in item:
    del item[key]
    print('Element with key "' + key + '" was successfully deleted')
    print(item)
else:
    print('There is no element with key "' + key + '" in dict')
