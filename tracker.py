import json
import os

def load_json(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_cheapest(data):
    result = {}

    for category in data["categories"].values():
        for store, products in category["stores"].items():
            seen = set()
            clean = []

            for p in products:
                norm = p["norm"]

                if "süd" not in norm:
                    continue
                if any(x in norm for x in ["ayran", "kefir", "kokos", "soya", "yulaf"]):
                    continue
                if norm in seen:
                    continue

                seen.add(norm)
                clean.append(p)

            if clean:
                cheapest = min(clean, key=lambda x: x["price"])
                result[store] = cheapest

    return result


def compare(old, new):
    changes = []

    for store, item in new.items():
        if store not in old:
            changes.append(f"{store}: yeni məhsul əlavə olundu ({item['name']} - {item['price']})")
        else:
            old_price = old[store]["price"]
            new_price = item["price"]

            if old_price != new_price:
                changes.append(
                    f"{store}: {item['name']} qiymət dəyişdi {old_price} → {new_price}"
                )

    return changes


# LOAD DATA
current_data = load_json("data.json")
history = load_json("history.json")

current_cheapest = get_cheapest(current_data)

# COMPARE
changes = compare(history, current_cheapest)

if changes:
    print("DƏYİŞİKLİK VAR:")
    for c in changes:
        print("-", c)
else:
    print("Heç bir dəyişiklik yoxdur")

# SAVE NEW STATE
save_json("history.json", current_cheapest)
