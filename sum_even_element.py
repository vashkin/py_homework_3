#  Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_event_element(number=0):
    res = 0
    resu = [number[i] for i in range(0, len(number)) if i % 2 > 0]
    for i in resu:
        res = i + res
    return res


number = 2, 3, 5, 9, 3
print(sum_event_element(number))
