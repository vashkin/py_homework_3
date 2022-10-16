
# Задача: Задайте число. Составьте список чисел
# Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def nega_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


list = [0]
in_data = int(input('Введите число: '))
for e in range(1, in_data + 1):
    list.append(fibonacci(e))
    list.insert(0, nega_fibonacci(e))
print(list)
