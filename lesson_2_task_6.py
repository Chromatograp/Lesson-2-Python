
print('Задача 6.')
# Вводим пустой список для заполнения пользователем:
product_list = []
# Вводим цикл для заполнения пользователем:
i = 1
while True:
    product_list.append(
        (input('Введите номер товара: '),
         dict(dict(Название=input('Введите название: '), Цена=float(input('Введите цену: ')),
                   Количество=int(input('Введите количество: ')), Ед=input('Введите единицы измерения: ')))))
    if input('Товар добавлен. Добавить еще один? да/нет ') == 'нет':
        break
    i += 1
# Выводим список, заполненный пользователем:
print('Список товаров: ')
print(product_list)
# Вводим пустой словарь для заполнения данными пользователя:
result_dict = dict({})
# Вводим цикл для заполнения словаря данными пользователя:
for product in product_list:
    for key, value in product[-1].items():
        if key in result_dict:
            if value not in result_dict.get(key):
                result_dict.get(key).append(value)
        else:
            result_dict.update({key: [value]})
# Выводим результат
print(result_dict)

