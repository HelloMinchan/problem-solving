# Write your MySQL query statement below
SELECT id,
    SUM(CASE WHEN month IN ("Jan") THEN revenue ELSE NULL END) AS Jan_Revenue,
    SUM(CASE WHEN month IN ("Feb") THEN revenue ELSE NULL END) AS Feb_Revenue,
    SUM(CASE WHEN month IN ("Mar") THEN revenue ELSE NULL END) AS Mar_Revenue,
    SUM(CASE WHEN month IN ("Apr") THEN revenue ELSE NULL END) AS Apr_Revenue,
    SUM(CASE WHEN month IN ("May") THEN revenue ELSE NULL END) AS May_Revenue,
    SUM(CASE WHEN month IN ("Jun") THEN revenue ELSE NULL END) AS Jun_Revenue,
    SUM(CASE WHEN month IN ("Jul") THEN revenue ELSE NULL END) AS Jul_Revenue,
    SUM(CASE WHEN month IN ("Aug") THEN revenue ELSE NULL END) AS Aug_Revenue,
    SUM(CASE WHEN month IN ("Sep") THEN revenue ELSE NULL END) AS Sep_Revenue,
    SUM(CASE WHEN month IN ("Oct") THEN revenue ELSE NULL END) AS Oct_Revenue,
    SUM(CASE WHEN month IN ("Nov") THEN revenue ELSE NULL END) AS Nov_Revenue,
    SUM(CASE WHEN month IN ("Dec") THEN revenue ELSE NULL END) AS Dec_Revenue
FROM Department
GROUP BY id