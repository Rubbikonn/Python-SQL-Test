-- Условие:
-- 1. Требуется составить расписание случайных проверок. Создайте оператор выбора, 
-- который выдаст 100 дат, начиная с текущей, при этом каждая дата отличается от предыдущей на 2-7 дней.

-- Решение:
SELECT generate_series(
  current_date,
  current_date + interval '100 days',
  interval '2 days' + random() * (interval '7 days' - interval '2 days')
) AS random_date;