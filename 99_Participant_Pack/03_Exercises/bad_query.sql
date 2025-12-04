/* CHALLENGE: OPTIMIZE THIS QUERY
   Scenario: This query takes 15 minutes to run on the Data Lake.
   Task: Paste it into Gemini/ChatGPT and ask: 
   "Why is this query slow and how can I optimize it for Athena?"
*/

-- Selecting everything is bad practice
SELECT * FROM pg_shrek_product_config AS c
JOIN pg_bob_product_config_attribute AS a 
    -- Cartesian product risk if IDs are not unique or indexed properly
    ON c.cod_sku = a.sku_id 
WHERE 
    -- CRIME #1: Applying a function on a column prevents index usage
    YEAR(DATE(c.created_at)) = 2024 
    
    -- CRIME #2: Inefficient Subquery
    AND c.cod_sku IN (
        SELECT sku 
        FROM product_stock_table 
        WHERE quantity > 0
    )
    
    -- CRIME #3: Vague filtering
    AND c.dsc_name_en LIKE '%Phone%'
