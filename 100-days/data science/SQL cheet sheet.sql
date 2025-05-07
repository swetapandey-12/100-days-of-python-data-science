-- ================================
-- 🛠️ Data Definition Language (DDL)
-- ================================

-- Create a new table
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(50)
);

-- Alter table: add column
ALTER TABLE customers ADD COLUMN email VARCHAR(100);

-- Rename column (PostgreSQL)
ALTER TABLE customers RENAME COLUMN city TO location;

-- Drop column
ALTER TABLE customers DROP COLUMN email;

-- Delete table
DROP TABLE customers;

-- ================================
-- 🧾 Data Manipulation Language (DML)
-- ================================

-- Insert data
INSERT INTO customers (id, name, age, location)
VALUES (1, 'John Doe', 28, 'New York');

-- Update data
UPDATE customers
SET age = 29
WHERE id = 1;

-- Delete data
DELETE FROM customers WHERE id = 1;

-- ================================
-- 📊 Select & Filtering Data
-- ================================

-- Select all rows
SELECT * FROM customers;

-- Select with condition
SELECT name FROM customers WHERE age > 25;

-- Multiple conditions
SELECT * FROM customers WHERE age > 25 AND location = 'New York';

-- Pattern matching
SELECT * FROM customers WHERE name LIKE 'J%';

-- IN clause
SELECT * FROM customers WHERE city IN ('NY', 'LA');

-- BETWEEN clause
SELECT * FROM customers WHERE age BETWEEN 20 AND 30;

-- ================================
-- 📐 Aggregate Functions
-- ================================

-- Count, Avg, Min, Max, Sum
SELECT COUNT(*) FROM customers;
SELECT AVG(age) FROM customers;
SELECT MIN(age), MAX(age) FROM customers;

-- Group by location
SELECT location, COUNT(*) FROM customers GROUP BY location;

-- Filter groups
SELECT location, COUNT(*) 
FROM customers 
GROUP BY location 
HAVING COUNT(*) > 5;

-- ================================
-- 🔗 Joins
-- ================================

-- Inner Join
SELECT a.name, b.order_id
FROM customers a
JOIN orders b ON a.id = b.customer_id;

-- Left Join
SELECT a.name, b.order_id
FROM customers a
LEFT JOIN orders b ON a.id = b.customer_id;

-- Right Join
SELECT a.name, b.order_id
FROM customers a
RIGHT JOIN orders b ON a.id = b.customer_id;

-- Full Join (PostgreSQL)
SELECT a.name, b.order_id
FROM customers a
FULL OUTER JOIN orders b ON a.id = b.customer_id;

-- ================================
-- 📦 Subqueries & CTEs
-- ================================

-- Subquery in WHERE
SELECT name FROM customers
WHERE id IN (SELECT customer_id FROM orders WHERE amount > 500);

-- Common Table Expression (CTE)
WITH high_spenders AS (
  SELECT customer_id, SUM(amount) AS total
  FROM orders
  GROUP BY customer_id
  HAVING SUM(amount) > 1000
)
SELECT * FROM high_spenders;

-- ================================
-- 🪟 Window Functions
-- ================================

-- ROW_NUMBER, RANK, DENSE_RANK
SELECT name, age,
  RANK() OVER (ORDER BY age DESC) AS age_rank
FROM customers;

-- Running total
SELECT name, salary,
  SUM(salary) OVER (ORDER BY id) AS running_total
FROM employees;

-- Partitioned average
SELECT department, salary,
  AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;

-- ================================
-- 🧠 Useful Data Science Queries
-- ================================

-- Top N records per group
SELECT * FROM (
  SELECT *, 
         ROW_NUMBER() OVER (PARTITION BY location ORDER BY age DESC) AS rn
  FROM customers
) sub
WHERE rn <= 3;

-- Correlated Subquery: Max order per customer
SELECT name, 
       (SELECT MAX(amount) FROM orders WHERE customer_id = c.id) AS max_order
FROM customers c;

-- Pivot-like aggregation
SELECT location,
  COUNT(*) AS total_customers,
  AVG(age) AS avg_age
FROM customers
GROUP BY location;

-- ================================
-- 🧹 Miscellaneous
-- ================================

-- Limit and Offset
SELECT * FROM customers LIMIT 10 OFFSET 20;

-- Null checks
SELECT * FROM customers WHERE email IS NULL;

-- CASE WHEN
SELECT name,
  CASE 
    WHEN age < 18 THEN 'Minor'
    WHEN age BETWEEN 18 AND 65 THEN 'Adult'
    ELSE 'Senior'
  END AS age_group
FROM customers;

-- Date functions (syntax may vary)
SELECT CURRENT_DATE;
SELECT AGE(CURRENT_DATE, birth_date) FROM customers;
