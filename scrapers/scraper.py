import json
import os
from datetime import datetime

def scrape_and_save():
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    data = {
        "last_updated": current_time,
        "categories": [
            {
                "category": "Süd",
                "products": [
                    {
                        "name": "Süd",
                        "brand": "Milla",
                        "details": "1 L",
                        "features": "2.5% yağlılıq",
                        "Bravo": 1.90,
                        "Araz": 2.10,
                        "Oba": 1.80
                    },
                    {
                        "name": "Süd",
                        "brand": "Milla",
                        "details": "1 L",
                        "features": "1.5% yağlılıq",
                        "Bravo": 1.80,
                        "Araz": 1.95,
                        "Oba": 1.70
                    },
                    {
                        "name": "Süd",
                        "brand": "AzərSüd",
                        "details": "1 L",
                        "features": "3.2% yağlılıq",
                        "Bravo": 2.05,
                        "Araz": 1.95,
                        "Oba": None
                    },
                    {
                        "name": "Süd",
                        "brand": "Alpina",
                        "details": "1 L",
                        "features": "3.5% yağlılıq",
                        "Bravo": 2.15,
                        "Araz": 2.10,
                        "Oba": 2.00
                    },
                    {
                        "name": "Süd",
                        "brand": "Bizim Tarla",
                        "details": "0.9 L",
                        "features": "2.5% yağlılıq",
                        "Bravo": 1.85,
                        "Araz": 1.80,
                        "Oba": 1.75
                    }
                ]
            },
            {
                "category": "Çörək",
                "products": [
                    {
                        "name": "Zavod çörəyi",
                        "brand": "Standart",
                        "details": "500 qr",
                        "features": "Ağ un",
                        "Bravo": 0.65,
                        "Araz": 0.65,
                        "Oba": 0.50
                    },
                    {
                        "name": "Təndir çörəyi",
                        "brand": "Ənənəvi",
                        "details": "600 qr",
                        "features": "İsti",
                        "Bravo": 0.90,
                        "Araz": 0.85,
                        "Oba": None
                    },
                    {
                        "name": "Kəpəkli çörək",
                        "brand": "Fidan",
                        "details": "450 qr",
                        "features": "Kəpəkli",
                        "Bravo": 0.70,
                        "Araz": 0.75,
                        "Oba": 0.60
                    }
                ]
            },
            {
                "category": "İçkilər",
                "products": [
                    {
                        "name": "Su",
                        "brand": "Sirab",
                        "details": "1.5 L",
                        "features": "Qazsız",
                        "Bravo": 0.80,
                        "Araz": 0.75,
                        "Oba": 0.70
                    },
                    {
                        "name": "Su",
                        "brand": "Sirab",
                        "details": "1.5 L",
                        "features": "Qazlı",
                        "Bravo": 0.85,
                        "Araz": 0.80,
                        "Oba": 0.75
                    },
                    {
                        "name": "Su",
                        "brand": "Badamlı",
                        "details": "1.5 L",
                        "features": "Qazsız",
                        "Bravo": 0.90,
                        "Araz": 0.85,
                        "Oba": 0.80
                    },
                    {
                        "name": "Qazlı içki",
                        "brand": "Coca-Cola",
                        "details": "1 L",
                        "features": "Şəkərli",
                        "Bravo": 1.50,
                        "Araz": 1.55,
                        "Oba": 1.40
                    },
                    {
                        "name": "Qazlı içki",
                        "brand": "Coca-Cola",
                        "details": "1 L",
                        "features": "Zero",
                        "Bravo": 1.60,
                        "Araz": 1.65,
                        "Oba": 1.45
                    },
                    {
                        "name": "Qazlı içki",
                        "brand": "Pepsi",
                        "details": "1 L",
                        "features": "Şəkərli",
                        "Bravo": 1.45,
                        "Araz": 1.50,
                        "Oba": 1.35
                    }
                ]
            },
            {
                "category": "Əsas ərzaqlar",
                "products": [
                    {
                        "name": "Şəkər tozu",
                        "brand": "Azərşəkər",
                        "details": "1 kq",
                        "features": "Ağ şəkər",
                        "Bravo": 1.50,
                        "Araz": 1.45,
                        "Oba": 1.35
                    },
                    {
                        "name": "Bitki yağı",
                        "brand": "Zeytun Bağları",
                        "details": "1 L",
                        "features": "Qarğıdalı",
                        "Bravo": 3.40,
                        "Araz": 3.50,
                        "Oba": None
                    },
                    {
                        "name": "Bitki yağı",
                        "brand": "Məryəm",
                        "details": "1 L",
                        "features": "Günəbaxan",
                        "Bravo": 3.10,
                        "Araz": 3.15,
                        "Oba": 3.00
                    },
                    {
                        "name": "Düyü",
                        "brand": "Bizim Tarla",
                        "details": "1 kq",
                        "features": "Ağ düyü",
                        "Bravo": 2.20,
                        "Araz": 2.25,
                        "Oba": 2.10
                    }
                ]
            }
        ]
    }
    
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", "prices.json")
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"Məlumatlar uğurla yeniləndi: {current_time}")

if __name__ == "__main__":
    scrape_and_save()
