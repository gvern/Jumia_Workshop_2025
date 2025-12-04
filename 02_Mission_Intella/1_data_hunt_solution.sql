-- Solution SQL example for Data Hunt
-- Find orders with suspicious prices (zero or negative)

SELECT order_id, sku, price, quantity, order_date
FROM orders
WHERE price <= 0
ORDER BY order_date DESC;
