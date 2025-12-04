-- Example of a slow/terrible query
SELECT o.order_id, o.customer_id, p.sku, p.price
FROM orders o, products p, customers c
WHERE o.product_id = p.id
AND o.customer_id = c.id
AND p.price * o.quantity > 1000
ORDER BY RAND();

-- Issues: old-style joins, non-optimized, ORDER BY RAND()
