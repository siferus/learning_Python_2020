number = 0
n = int(input('Введите n: '))

while number <= n:
    if number % 2 == 0:
        # не делятся на 2, т.е. нечетные числа if number % 2 != 0:
        print(number)
    number += 1

