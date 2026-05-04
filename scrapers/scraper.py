import json
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_and_save():
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    # Əsas struktur
    data = {
        "last_updated": current_time,
        "categories": [
            {
                "category": "Süd və Süd məhsulları",
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
                        "brand": "AzərSüd",
                        "details": "1 L",
                        "features": "3.2% yağlılıq",
                        "Bravo": 2.05,
                        "Araz": 1.95,
                        "Oba": None
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
                    }
                ]
            }
        ]
    }
    
    # Saytdan real skrap etmək üçün hissə
    try:
        # url = "https://sizin-sayt.az"
        # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        # response = requests.get(url, headers=headers)
        # 
        # if response.status_code == 200:
        #     soup = BeautifulSoup(response.text, "html.parser")
        #     data["categories"][0]["products"] = []  # Köhnə siyahını təmizləyirik
        #     
        #     # Saytdakı məhsul kartlarını tapıb dövrə salırıq
        #     for item in soup.find_all("div", class_="product-card"):
        #         name = item.find("h3", class_="product-title").text.strip()
        #         brand = item.find("span", class_="brand").text.strip()
        #         price = float(item.find("span", class_="price").text.replace("AZN", "").strip())
        #         
        #         data["categories"][0]["products"].append({
        #             "name": name,
        #             "brand": brand,
        #             "details": "1 L",
        #             "features": "Standart",
        #             "Bravo": price,
        #             "Araz": price + 0.10,
        #             "Oba": price - 0.20
        #         })
        pass
        
    except Exception as e:
        print(f"Skrepinq zamanı xəta baş verdi: {e}")

    # Faylın yaradılması və yazılması
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", "prices.json")
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"Məlumatlar uğurla yeniləndi və yadda saxlanıldı: {current_time}")

if __name__ == "__main__":
    scrape_and_save()
