-- Условие:
-- 3. Имеется таблица денежных переводов transfers.
-- from – номер аккаунта, с которого сделан перевод,
-- to – номер аккаунта, на который сделан перевод,
-- amount – сумма перевода,
-- tdate – дата перевода.
-- Требуется создать оператор выбора, который для каждого аккаунта выведет периоды постоянства остатков. 
-- Результат запроса должен содержать столбцы acc – номер аккаунта, dt_from - начало периода,
-- dt_to - конец периода, balance – остаток на счёте в данном периоде.
-- Дата конца последнего периода – 01.01.3000. 

-- Решение:
SELECT 
    acc AS acc,
    dt_from,
    LEAD(dt_from, 1, '3000-01-01'::date) OVER (PARTITION BY acc ORDER BY dt_from) AS dt_to,
    balance
FROM (
    SELECT 
        acc,
        tdate AS dt_from,
        LAG(tdate, 1, '2000-01-01'::date) OVER (PARTITION BY acc ORDER BY tdate) + 1 AS prev_dt_to,
        balance
    FROM (
        SELECT 
            from AS acc,
            tdate,
            SUM(amount) OVER (PARTITION BY from ORDER BY tdate) AS balance
        FROM transfers
    ) AS subquery
) AS subquery2
WHERE dt_from > prev_dt_to
ORDER BY acc, dt_from;