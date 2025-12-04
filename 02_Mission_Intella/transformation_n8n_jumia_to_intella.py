"""
Transformation script for n8n (Python Code node)

Converts Jumia raw product records into the Intella JSON shape according to the workshop PDF.

Key rules implemented:
- Exclude products with stock <= 0
- Build category with ' > ' separator from category name parts
- Map fields according to spec and set currency to EGP (POC)
"""

def _to_number(v):
    if v is None:
        return None
    try:
        # accept numbers or numeric strings
        return float(v)
    except Exception:
        return None


def transform_input_to_intella(items):
    output = []
    for it in items:
        # support n8n input item shape: { 'json': {...} } or raw dict
        product = it.get("json") if isinstance(it, dict) and "json" in it else it

        stock_raw = product.get("mtr_stock", 0)
        stock_num = _to_number(stock_raw)
        if stock_num is None or stock_num <= 0:
            # rule: only include products with stock > 0
            continue

        cat_parts = [
            product.get("dsc_category_name_1"),
            product.get("dsc_category_name_2"),
            product.get("dsc_category_name_3"),
        ]
        full_category = " > ".join([c for c in cat_parts if c])

        is_express = product.get("dsc_custom_label_one") in (1, "1", True, "true", "True")

        transformed_product = {
            "sku_id": product.get("cod_sku"),
            "title": product.get("dsc_name_en", product.get("dsc_name_fr", "Unknown")),
            "price": product.get("mtr_price"),  # Sale price
            "currency": "EGP",
            "stock_status": "in_stock" if stock_num > 0 else "out_of_stock",
            "category": full_category,
            "brand": product.get("dsc_brand_name"),
            "image_url": product.get("dsc_url_image"),
            "is_express": bool(is_express),
        }

        output.append({"json": transformed_product})

    return output


# n8n compatibility: when executed inside n8n, `items` is provided
try:
    if "items" in globals():
        return_data = transform_input_to_intella(items)
except Exception:
    pass


if __name__ == "__main__":
    # quick local test
    sample_items = [
        {"json": {"cod_sku": "SAM-S24-BLK", "mtr_stock": 150, "dsc_name_en": "Samsung Galaxy S24 Ultra", "dsc_original_price": 1200.0, "mtr_price": 999.0, "dsc_brand_name": "Samsung", "dsc_url_image": "https://dz.jumia.is/12abc/SAM-S24-BLK.jpg", "dsc_category_name_1": "Phones", "dsc_category_name_2": "Mobile Phones", "dsc_custom_label_one": 1}},
        {"json": {"cod_sku": "ANOM-OUT-01", "mtr_stock": 0, "dsc_name_en": "Out of Stock Example", "dsc_original_price": 100.0, "mtr_price": 80.0, "dsc_brand_name": "BrandX", "dsc_url_image": "https://dz.jumia.is/12abc/ANOM-OUT-01.jpg", "dsc_category_name_1": "Phones", "dsc_category_name_2": "Mobile Phones", "dsc_custom_label_one": 0}},
    ]

    import json

    print("Input sample:")
    print(json.dumps(sample_items, indent=2))
    print("\nTransformed output:")
    print(json.dumps(transform_input_to_intella(sample_items), indent=2))
