import json
import os
from datetime import datetime

def scrape_and_save():
    # Tarixi avtomatik yeniləyirik
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    data = {
        "last_updated": current_time,
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
            },
            {
                "category": "Çörək",
                "brand": "Zavod",
                "details": "500 qr",
                "Bravo": 0.65,
                "Araz": 0.65,
                "Oba": 0.50
            },
            {
                "category": "Su (Qazsız)",
                "brand": "Sirab",
                "details": "1.5 L",
                "Bravo": 0.80,
                "Araz": 0.75,
                "Oba": 0.70
            },
            {
                "category": "Qazlı içki",
                "brand": "Coca-Cola",
                "details": "1 L",
                "Bravo": 1.50,
                "Araz": 1.55,
                "Oba": 1.40
            },
            {
                "category": "Şəkər tozu",
                "brand": "Azərşəkər",
                "details": "1 kq",
                "Bravo": 1.50,
                "Araz": 1.45,
                "Oba": 1.35
            },
            {
                "category": "Bitki yağı",
                "brand": "Zeytun Bağları",
                "details": "1 L",
                "Bravo": 3.40,
                "Araz": 3.50,
                "Oba": None
            }
        ]
    }
    
    # Faylın saxlanacağı qovluğu yaradırıq
    os.makedirs("data", exist_ok=True)
    
    file_path = os.path.join("data", "prices.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"Məlumatlar uğurla yeniləndi: {current_time}")

if __name__ == "__main__":
    scrape_and_save()
