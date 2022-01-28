ale = 71
age = int(input('Сколько Вам лет:'))

after20 = age + 20
print('Через 20 лет Вам будет', after20)

alive = ale - age
print('Вам осталось жить', alive)

count = 144000000
all_live = count * ale
print('Средняя продолжительность жизни', all_live)

live_part = age / ale
print('Часть прожитой жизни', live_part)

print(type(live_part))

#целая часть от деления
live_part = age // ale
print('Часть прожитой жизни', live_part)

#остаток от деления\
print(3%2)
print(4%2)
print(5%3)

#возведение в степень
print(2**10)
print(2**2)

