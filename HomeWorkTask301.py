# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

num = [2, 3, 5, 9, 3]
count = 0
for i in range(0, len(num)):
    if i % 2 != 0:
        count += num[i]
print(count)
