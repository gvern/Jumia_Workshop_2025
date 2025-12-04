-- Optimized query suggestion
SELECT o.order_id, o.customer_id, p.sku, p.price
FROM orders o
JOIN products p ON o.product_id = p.id
JOIN customers c ON o.customer_id = c.id
WHERE p.price * o.quantity > 1000
ORDER BY o.order_date DESC 
LIMIT 100;

-- Notes: use explicit JOINs, order by indexed column, remove RAND(), limit results
