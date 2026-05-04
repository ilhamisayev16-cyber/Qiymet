import json
import os

# Yeni məlumat modeli
data = {
    "last_updated": "04.05.2026 18:21", # Tarixi avtomatik yeniləmək üçün Python time/datetime kitabxanasını istifadə edə bilərsiniz
    "items": [
        {
            "category": "Süd",
            "brand": "Milla",
            "details": "1 L, 2.5%",
            "Bravo": 1.90,
            "Araz": 2.10,
            "Oba": 1.80
        },
        {
            "category": "Süd",
            "brand": "AzərSüd",
            "details": "1 L, 3.2%",
            "Bravo": 2.05,
            "Araz": 1.95,
            "Oba": None
        }
    ]
}

# Faylı yadda saxlamaq
os.makedirs("data", exist_ok=True)
with open("data/prices.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
