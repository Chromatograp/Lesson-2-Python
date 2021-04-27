
print('Задача 3.')

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
year = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
if d in year['winter']:
    print("Это зимний месяц")
elif d in year['spring']:
    print("Это весенний месяц")
elif d in year['summer']:
    print("Это летний месяц")
elif d in year['autumn']:
    print("Это осенний месяц")
else:
    print('В году нет столько месяцев')