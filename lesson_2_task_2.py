from itertools import chain

print('Задача 2.')

# первый вариант решения
a = list(input('Введите строку '))
print(list(chain(*(x for x in zip(a[1::2], a[::2])))))

# второй вариант решения
if len(a) % 2 == 0:
        a[::2], a[1::2] = a[1::2], a[::2]
        print('Ваша строка содержит четное число элементов', a)
else:
        index = -1
        b = a[:index]
        b[::2], b[1::2] = b[1::2], b[::2]
        b.extend(a[index])
        print('Ваша строка содержит нечетное число элементов', b)