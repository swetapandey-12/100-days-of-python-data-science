# Write your MySQL query statement below
SELECT e1.name AS Employee
from Employee e1 left join Employee e2 
ON e1.managerid = e2.Id
where e1.salary>e2.salary
