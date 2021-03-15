from typing import List

my_list = ['собака', 'кошка', 76, 32]

print(my_list)
print(type(my_list))
for letter in my_list:
    print(letter)
    print(type(letter))

a = list(input('Введите строку'))

print(a[1:-1], a[::-1], a[::2])

c = str(input('Введите предложение'))
for letter in c.split():
    if len(letter) > 10:
        print(letter[:10])
    else:
        print(letter)