import json

data = {
    "Bravo": {"name": "Süd", "price": 1.79},
    "Neptun": {"name": "Süd", "price": 2.55},
    "OBA": {"name": "Süd", "price": 2.57}
}

with open("prices.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("prices.json hazırdır")
