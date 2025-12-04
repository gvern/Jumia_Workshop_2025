
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
	import json
	import csv
	import os

	# Load data from the participant pack CSV
	csv_path = os.path.join(os.path.dirname(__file__), "..", "99_Participant_Pack", "01_Data_Samples", "intella_sample.csv")
	
	items = []
	with open(csv_path, 'r', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		for row in reader:
			# Convert numeric fields
			for field in ['mtr_stock', 'dsc_original_price', 'mtr_price', 'mtr_price_discount', 'mtr_rating_count', 'mtr_rating', 'mtr_seller_score', 'dsc_custom_label_one']:
				if field in row and row[field]:
					try:
						row[field] = float(row[field]) if '.' in str(row[field]) else int(row[field])
					except:
						pass
			items.append({"json": row})
	
	print(f"Loaded {len(items)} products from CSV")
	print("\n" + "="*50)
	print("TRANSFORMATION RESULTS")
	print("="*50 + "\n")
	
	transformed = transform_items(items)
	
	print(f"✓ Filtered to {len(transformed)} products (excluded stock <= 0)")
	print("\nClean JSON Output:\n")
	print(json.dumps(transformed, indent=2, ensure_ascii=False))

