-- Условие:
-- 2. Требуется оценить эффективность продавцов. Создайте запрос, который вернёт количество и 
-- сумму продаж для каждого продавца, а также ранжирует продавцов по количеству продаж и по сумме продаж.
-- Результат запроса должен содержать столбцы id, name из таблицы employee, а также столбцы:
-- sales_c - количество продаж, 
-- sales_rank_c - ранг по количеству продаж, 
-- sales_s - сумма продаж, 
-- sales_rank_s -  ранг по сумме продаж.
-- Решение:

WITH sales_summary AS (
  SELECT 
    employee_id,
    COUNT(*) AS sales_c,
    SUM(price) AS sales_s,
    RANK() OVER (ORDER BY COUNT(*) DESC) AS sales_rank_c,
    RANK() OVER (ORDER BY SUM(price) DESC) AS sales_rank_s
  FROM sales
  GROUP BY employee_id
)
SELECT 
  e.id,
  e.name,
  s.sales_c,
  s.sales_rank_c,
  s.sales_s,
  s.sales_rank_s
FROM employee e
JOIN sales_summary s ON e.id = s.employee_id
ORDER BY s.sales_rank_c, s.sales_rank_s;