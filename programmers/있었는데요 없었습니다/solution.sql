-- 코드를 입력하세요
SELECT AO.ANIMAL_ID, AO.NAME
FROM ANIMAL_OUTS AS AO
LEFT JOIN ANIMAL_INS AS AI
USING(ANIMAL_ID)
WHERE AO.DATETIME < AI.DATETIME
ORDER BY AI.DATETIME;