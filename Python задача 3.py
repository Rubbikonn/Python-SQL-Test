from itertools import permutations
# Условие:
# 3. Напишите функцию, которая принимает на вход список строк, состоящих из цифр,
# и возвращает максимальное возможное число, 
# которое может получиться в результате конкатенации всех строк из этого списка.

# Решение:
# Тестовые переменные:
a = ['41', '4', '005', '89']
# Функция:
def concat_max_number(list_of_strings):

  intermadiate_list = []
  
  for i in list_of_strings:
    if not i.isdigit():
      return print('В данном списке не все элементы являются строками, состоящими из цифр')

  all_combinations = list(permutations(list_of_strings))
  for i in all_combinations:
    tuple = list(i)
    number = ''.join(tuple)
    intermadiate_list.append(number)

  result_list = list(map(int, intermadiate_list))

  return max(result_list)

# Тестовый вывод:
  
print(concat_max_number(a))