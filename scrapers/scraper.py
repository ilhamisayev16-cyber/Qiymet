import json
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def main():
    # Vaxtı götürürük
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    # Saytınızın çökməməsi üçün baza məlumatlar
    data = {
        "last_updated": current_time,
        "categories": [
            {
                "category": "Süd və Süd məhsulları",
                "products": [
                    {"name": "Süd", "brand": "Milla", "details": "1 L | 2.5%", "Bravo": 1.90, "Araz": 2.10, "Oba": 1.80},
                    {"name": "Süd", "brand": "AzərSüd", "details": "1 L | 3.2%", "Bravo": 2.05, "Araz": 1.95, "Oba": 0}
                ]
            },
            {
                "category": "İçkilər",
                "products": [
                    {"name": "Su", "brand": "Sirab", "details": "1.5 L | Qazsız", "Bravo": 0.80, "Araz": 0.75, "Oba": 0.70}
                ]
            }
        ]
    }

    # Bura gələcəkdə real saytlardan avtomatik qiymət çəkmək üçün kodlar əlavə edəcəyik.
    # Hazırda skript errorsuz işləsin deyə yuxarıdakı bazadan istifadə edirik.

    # Data qovluğunu yaradırıq (əgər yoxdursa)
    os.makedirs("data", exist_ok=True)
    
    # JSON faylını yaradıb məlumatları içinə yazırıq
    file_path = os.path.join("data", "prices.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"Əla! prices.json faylı xətasız yaradıldı və yeniləndi: {current_time}")

if __name__ == "__main__":
    main()
