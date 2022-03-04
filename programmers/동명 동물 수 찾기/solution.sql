-- 코드를 입력하세요
SELECT NAME, COUNT(*) AS "COUNT" FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME HAVING COUNT(*) > 1 ORDER BY NAME;

-- 코드를 입력하세요
select name, count
from (select name, count(*) as "count" from animal_ins group by name having name is not null) as sub_table
where count >= 2
order by name;