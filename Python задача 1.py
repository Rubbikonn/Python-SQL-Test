import re
# Условие задачи:

# 1. Особенный номер – строка формата [2-4 цифры]\[2-5 цифр]. 
# Хороший номер - строка формата [4 цифры]\[5 цифр]. Хороший номер можно получить из особенного 
# дополнением нулей слева к обоим числам.
# Пример:
# 17\234 => 0017\00234 
# Напишите функцию, которая принимает на вход строку и для 
# каждого особенного номера, встречающегося в строке, выводит соответствующий хороший номер.

# Решение:

# Тестовая строка:
a = r'Адрес 5467\456. Номер 405\549'
# Функция:
def transform_numbers(input_string):
  pattern = r'\d{2,4}\\\d{2,5}'
  check_special_number = re.findall(pattern, input_string)

  if check_special_number:
    for item in check_special_number:
      first_part = item.split('\\')[0].zfill(4)
      second_part = item.split('\\')[1].zfill(5)
      final_number = f'{first_part}\\{second_part}'
      print(final_number)
  else:
    print('Во введённой Вами строке нет особенных номеров')

  return('Выше Вы видите все хорошие номера, которые получились из особенных номеров')

# Тестовый вывод:
    
print(transform_numbers(a))