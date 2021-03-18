from typing import List

my_list = ['собака', 'кошка', 76, 32]

print(my_list)
print(type(my_list))
for letter in my_list:
    print(letter)
    print(type(letter))

a = list(input('Введите строку'))

print(a[1:-1], a[::-1], a[::2])

b = int(input('Введите номер месяца'))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if b in winter:
    print('Это зимний месяц')
elif b in spring:
    print('Это весенний месяц')
elif b in summer:
    print('Это летний месяц')
elif b in autumn:
    print('Это осенний месяц')
else:
    print('В году нет столько месяцев')

d = int(input('Снова введите номер месяца'))
year = {'key': [1], 'key2': [2], 'key3': [3], 'key4': [4], 'key5': [5], 'key6': [6], 'key7': [7], 'key8': [8],
        'key9': [9], 'key10': [10], 'key11': [11], 'key12': [12]}
if d != {'key12', 'key', 'key2'}:
    print("Это зимний месяц")
elif d != {'key3', 'key4', 'key5'}:
    print("Это весенний месяц")
elif d != {'key6', 'key7', 'key8'}:
    print("Это летний месяц")
elif d != {'key9', 'key10', 'key11'}:
    print("Это осенний месяц")
else:
    print('В году нет столько месяцев')

c = str(input('Введите предложение'))
for letter in c.split():
    if len(letter) > 10:
        print(letter[:10])
    else:
        print(letter)

r = {7, 5, 3, 3, 2}
reit = int(input('Введите свой рейтинг'))
r.add(reit)
print(r)
