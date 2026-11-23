.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- 1. List every column for every driver.

.schema drivers

-- 2. List the name and price of every dish sold by Bangkok Garden (restaurant 3).

SELECT name, price FROM menu_items
WHERE restaurant_id = 3;

-- 3. List the names of all the Indian restaurants.

SELECT name FROM restaurants
WHERE cuisine = 'Indian';

-- 4. How many customers does Leeds Eats have?

SELECT COUNT(*) as number_of_customers FROM customers;

-- 5. **A student:** "I'm vegetarian and I've only got £8. What could I order? Cheapest first, please."

SELECT name, price FROM menu_items
WHERE is_vegetarian = 1 AND price <= 8 
ORDER BY price ASC;

-- 6. **A food safety officer from Leeds City Council:** "Which restaurants have a hygiene rating below 4? Show the worst first."

SELECT name, hygiene_rating FROM restaurants
WHERE hygiene_rating < 4
ORDER BY hygiene_rating ASC;

-- 7. **A student who lives in LS6:** "Which restaurants are near me, best rated first?" Does a matching postcode really mean a restaurant is near? What could go wrong?

SELECT name, hygiene_rating FROM restaurants
WHERE postcode LIKE 'LS6%'
ORDER BY hygiene_rating DESC;

-- 8. **The marketing team:** "We want to email everyone who signed up with a University of Leeds email address, newest members first." 
--      Write the query, then say whether Leeds Eats should actually send this email.

SELECT email, joined_date FROM customers
WHERE email LIKE '%@leeds.ac.uk'
ORDER BY joined_date DESC;

-- 9. **The operations manager:** "Show me the 10 most recent cancelled orders."

SELECT order_id, order_time FROM orders
WHERE status = 'cancelled'
ORDER BY order_time DESC
LIMIT 10;

-- 10. **The owner of Pasta Pronto (restaurant 4):** "Which of my dishes are vegetarian? And what's my most expensive dish?" (Two queries.)

SELECT name FROM menu_items
WHERE restaurant_id = 4 AND is_vegetarian = 1;

SELECT name as Most_Expensive FROM menu_items
WHERE restaurant_id = 4 
ORDER BY price DESC
LIMIT 1;

-- 11. **The operations manager:** "Some orders from October look stuck: they still say 'placed'. Find them for the support team." 
--          Choose only the columns a support agent would need, and justify each one.

SELECT order_id FROM orders
WHERE status = 'placed' and order_time LIKE '2026-10%';

-- 12. **A colleague:** "I want the 5 cheapest vegetarian dishes. My first query gives an error and my second gives the wrong answer. Why?"
   
--      SELECT name, price FROM menu_items ORDER BY price LIMIT 5 WHERE is_vegetarian = 1; -- WHERE should come before ORDER BY
--      SELECT name, price FROM menu_items WHERE is_vegetarian = 1 LIMIT 5; -- ORDER BY needs to be set to ASC
   
--   Explain what's wrong with each, then write a correct version.

SELECT name, price FROM menu_items
WHERE is_vegetarian = 1 
ORDER BY price ASC
LIMIT 5;

-- 13. **A customer:** "What's the cheapest thing I can get on Leeds Eats?" Write the query. Then run it again with LIMIT 5 instead of LIMIT 1. 
--      What do you notice, and how should Leeds Eats answer this customer fairly? -- List all items at price 3.5

SELECT name, price FROM menu_items
ORDER BY price ASC
LIMIT 5;

