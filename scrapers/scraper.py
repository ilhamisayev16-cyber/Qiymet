import requests
import json
import re
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

STORES = {
    "Bravo":  "bravo-supermarket-globus-centre",
    "Neptun": "neptun-supermarket-28",
    "Rahat":  "rahat-supermarket-heydar-aliyev",
    "OBA":    "oba-market-nerimanov-1",
}

CATEGORIES = [
    {"id": "sud", "name": "Süd 1L", "queries": ["sud", "milk", "1l"]}
]


# --- helperlər ---
def normalize_name(name):
    name = name.lower()
    name = name.replace(",", ".")
    name = re.sub(r"\s+", " ", name)
    return name.strip()


def search_items(slug, query):
    try:
        url = f"https://consumer-api.wolt.com/consumer-api/consumer-assortment/v1/venues/slug/{slug}/assortment/items/search?language=az"
        r = requests.post(url, headers=HEADERS, json={"q": query}, timeout=10)
        if r.status_code != 200:
            return []
        data = r.json()
        return data.get("items") or data.get("results") or []
    except:
        return []


def extract_price(item):
    p = item.get("price") or item.get("baseprice")
    if isinstance(p, dict):
        p = p.get("amount")
    if isinstance(p, (int, float)):
        return round(p / 100, 2)
    return None


def extract_name(item):
    n = item.get("name")
    if isinstance(n, dict):
        return n.get("az") or n.get("en")
    return str(n)


# --- əsas ---
final = {}

for cat in CATEGORIES:
    cat_data = {}

    for store, slug in STORES.items():
        all_items = []

        for q in cat["queries"]:
            all_items += search_items(slug, q)

        products = []

        for item in all_items:
            name = extract_name(item)
            if not name:
                continue

            if "süd" not in name.lower() and "sud" not in name.lower():
                continue

            if "1l" not in name.lower() and "1 l" not in name.lower():
                continue

            price = extract_price(item)
            if not price:
                continue

            products.append({
                "name": name,
                "norm": normalize_name(name),
                "price": price
            })

        cat_data[store] = products

    final[cat["id"]] = {
        "name": cat["name"],
        "stores": cat_data
    }


output = {
    "last_updated": datetime.now().strftime("%d %B %Y, %H:%M"),
    "categories": final
}

with open("data/prices.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("DONE")
