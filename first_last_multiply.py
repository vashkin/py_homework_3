# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def first_last_multiply(number):
    res = []
    for i in range(1, (len(number))-1):
        res.append(number[i-1]*number[-i])
    return res


number = [2, 3, 4, 5, 6]
print(first_last_multiply(number))
