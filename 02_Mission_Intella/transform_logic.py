
"""
Transformation Logic based on "Intella Product Feed.docx"

This script is n8n-compatible. In the n8n Python Code node use `_input.all()`.
When run standalone it performs a basic self-test.
"""

def _to_float(v):
	try:
		if v is None:
			return None
		if isinstance(v, (int, float)):
			return float(v)
		s = str(v).strip()
		if s == "":
			return None
		return float(s)
	except Exception:
		return None


def transform_items(input_items):
	output_data = []
	for item in input_items:
		product = item.get("json") if isinstance(item, dict) and "json" in item else item

		# --- QUALITY GATES ---
		stock = _to_float(product.get("mtr_stock", 0)) or 0
		if stock <= 0:
			# Rule: Stock > 0 required
			continue

		# --- CATEGORY HIERARCHY (l1..l8) ---
		cat_parts = []
		for i in range(1, 9):
			val = product.get(f"dsc_category_name_l{i}")
			if val:
				cat_parts.append(val)
		full_category = " > ".join(cat_parts)

		# --- Jumia Express ---
		is_express = 1 if str(product.get("dsc_custom_label_one")).strip() == '1' else 0

		# --- SIMPLE SKU construction ---
		base_sku = product.get("cod_sku", "UNKNOWN")
		size = product.get("dsc_size")
		simple_sku = f"{base_sku}-{size}" if size else base_sku

		# --- MAPPING ---
		mapped_product = {
			"SKU": base_sku,
			"simple_sku": simple_sku,
			"stock": int(stock),
			"Title": product.get('dsc_name_en') or product.get('dsc_name_fr') or "No Title",
			"URL": product.get('dsc_product_url'),
			"imageUrl": product.get('dsc_url_image'),
			"originalPrice": product.get('dsc_original_price'),
			"salePrice": product.get('mtr_price'),
			"discount": product.get('mtr_price_discount'),
			"brand": product.get('dsc_brand_name'),
			"category": full_category,
			"is_express": is_express,
			"rating": product.get('mtr_rating'),
			"rating_count": product.get('mtr_rating_count'),
			"model": product.get('attr_model'),
			"warranty": product.get('attr_warranty_duration'),
		}

		output_data.append({"json": mapped_product})

	return output_data


# n8n compatibility: use _input.all() inside n8n Python Code node
try:
	if "_input" in globals():
		items = _input.all()
		return_data = transform_items(items)
except Exception:
	# ignore in non-n8n contexts
	pass


if __name__ == "__main__":
	# quick local test
	sample = [
		{"json": {"cod_sku": "IPH-15-PRO", "mtr_stock": 50, "dsc_name_en": "iPhone 15 Pro 128GB", "dsc_product_url": "https://jumia.is/p/1", "dsc_url_image": "https://jumia.is/img/1.jpg", "dsc_original_price": 1200.0, "mtr_price": 999.0, "mtr_price_discount": 17, "mtr_rating_count": 150, "mtr_rating": 4.8, "dsc_brand_name": "Apple", "dsc_size": "128GB", "dsc_color_family": "Titanium", "dsc_category_name_l1": "Phones & Tablets", "dsc_category_name_l2": "Mobile Phones", "dsc_category_name_l3": "Smartphones", "dsc_custom_label_one": 1, "mtr_seller_score": 4.5, "attr_model": "iPhone 15", "attr_warranty_duration": "1 Year"}},
		{"json": {"cod_sku": "SAM-S24-ULT", "mtr_stock": 0, "dsc_name_en": "Samsung S24 Ultra", "dsc_product_url": "https://jumia.is/p/2", "dsc_url_image": "https://jumia.is/img/2.jpg", "dsc_original_price": 1400.0, "mtr_price": 1100.0, "mtr_price_discount": 21, "mtr_rating_count": 80, "mtr_rating": 4.7, "dsc_brand_name": "Samsung", "dsc_size": "256GB", "dsc_color_family": "Black", "dsc_category_name_l1": "Phones & Tablets", "dsc_category_name_l2": "Mobile Phones", "dsc_category_name_l3": "Smartphones", "dsc_custom_label_one": 1, "mtr_seller_score": 4.2, "attr_model": "S24 Ultra", "attr_warranty_duration": "2 Years"}},
	]

	import json
	print("Input sample:")
	print(json.dumps(sample, indent=2))
	print("\nTransformed output:")
	print(json.dumps(transform_items(sample), indent=2))

