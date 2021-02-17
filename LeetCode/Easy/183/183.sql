# Write your MySQL query statement below
SELECT Name AS Customers
FROM Customers
LEFT JOIN Orders
ON Customers.id = Orders.CustomerId
WHERE Orders.id IS NULL