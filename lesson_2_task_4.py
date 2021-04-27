
print('Задача 4.')

c = str(input('Введите предложение'))
n = 0
for letter in c.split():
    n += 1
    if len(letter) > 10:
        print(n, letter[:10])
    else:
        print(n, letter)