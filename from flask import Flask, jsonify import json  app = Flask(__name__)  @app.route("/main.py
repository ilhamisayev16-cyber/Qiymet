import json

# sənin böyük data faylın
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

result = {}

for category in data["categories"].values():
    for store, products in category["stores"].items():

        seen = set()
        clean = []

        for p in products:
            norm = p["norm"]

            # yalnız süd saxla
            if "süd" not in norm:
                continue
            if any(x in norm for x in ["ayran", "kefir", "kokos", "soya", "yulaf"]):
                continue

            # duplicate sil
            if norm in seen:
                continue
            seen.add(norm)

            clean.append(p)

        if clean:
            cheapest = min(clean, key=lambda x: x["price"])
            result[store] = {
                "name": cheapest["name"],
                "price": cheapest["price"]
            }

# sayta veriləcək fayl
with open("prices.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print("Hazırdır → prices.json")
