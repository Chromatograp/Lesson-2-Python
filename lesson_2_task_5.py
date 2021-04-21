
print('Задача 5.')

my_rating = [7, 5, 3, 3, 2]
print('Рейтинг', my_rating)
i = 0
# Считаем количество элементов одного типа в списке:
for el in my_rating:
    if i >= 10:
        break
    else:
        i += 1
        count = my_rating.count(i)
# Выводим значение, количество и порядковый номер первого элемента для повторяющихся элементов:
        if i in my_rating and count >= 2:
            value = i
            num = count
            index = my_rating.index(i)
        else:
            pass
# Складываем количество и порядковый номер первого из повторяющихся элементов,
# чтобы найти порядковый номер добавленного числа:
place = int(num) + int(index)

your_rating = int(input('Введите свой рейтинг '))
# Теперь можно разделить варианты действий для случаев, если значение совпадает
# с повторяющимся элементом или не совпадает:
if your_rating == value:
    my_rating.insert(place, your_rating)
else:
    my_rating.append(your_rating)
print('Рейтинг вместе с вашей оценкой', my_rating)