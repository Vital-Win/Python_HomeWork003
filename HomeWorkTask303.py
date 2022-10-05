# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением 
# дробной части элементов.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5, 10.01]
new_lst = [i%1 for i in lst]
subtraction = max(new_lst) - min(new_lst)
subtraction_str = str(subtraction)
my_result = subtraction_str[:4]
print(f'Наш список: \n{lst}')
print(f'\nРазница между min и max значениями дробной части элементов: \n{my_result}')
