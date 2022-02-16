/*
Enter your query here.
*/
SELECT IF(G.GRADE < 8, NULL, S.NAME), G.GRADE, S.MARKS
FROM STUDENTS AS S, GRADES AS G
WHERE S.MARKS BETWEEN G.MIN_MARK AND G.MAX_MARK
ORDER BY G.GRADE DESC, S.NAME, S.MARKS;