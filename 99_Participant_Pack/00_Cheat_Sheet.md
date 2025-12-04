# Jumia Data & AI Workshop - Survival Guide

## 🟢 Module 1: Blind Discovery (The Data Hunt)
**Context:** You are a new Joiner. You have no documentation, only Table Names.
**Your Goal:** Find the right data for the Intella Feed.

**Available Tables:**
1. `pg_shrek_product_config` (Main Product Info)
2. `product_simple` (Variations: Size, Color)
3. `stock_inventory` (Quantities)

**🏆 The Golden Prompt (Try this in Gemini/Dust):**
> "I act as a Data Engineer at Jumia. I have these table names: [Insert Table Names].
> I need to create a flat feed containing: SKU, Product Name, Price, Stock, and Image URL.
> 
> Can you write a SQL query for AWS Athena that:
> 1. Joins these tables logically (guess the join keys, usually 'sku' or 'id').
> 2. Filters only products with Stock > 0.
> 3. Selects the specific columns required."

---

## 🟠 Module 2: The Transformation (Python in n8n)
**Context:** You need to format the data to match the Intella JSON specification.

**Key Python Snippet for n8n:**
If you need to filter stock or create the 'Category > Subcategory' string, ask the AI:
> "Write a Python script for n8n that takes a JSON input.
> - Input fields: `dsc_category_name_l1`, `dsc_category_name_l2`.
> - Logic: Join them with a ' > ' separator. Ignore empty fields.
> - Output field: `full_category`."

---

## 🔴 Module 3: SOX Quality Gate (The Agent)
**Context:** Stop bad data before it leaves Jumia.

**Risk Checklist (To Implement):**
[ ] **Zero Price Check:** Is `sale_price` <= 0?
[ ] **Missing Image:** Is `image_url` empty?
[ ] **Stock Inconsistency:** Is `stock` > 0 but status is 'Out of Stock'?
