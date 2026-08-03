import requests
from bs4 import BeautifulSoup

def abituriyent_malumotini_olish(abituriyent_id):
    # 1-qadam: Avval Qidiruv sahifasiga ID bilan murojaat qilamiz
    search_url = f"https://mandat.uzbmb.uz/Bakalavr?name={abituriyent_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(search_url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Saytdagi jadvallar orasidan 'hashId' yashiringan ssilkani qidiramiz
            link = soup.find('a', href=lambda href: href and "hashId=" in href)
            
            if link:
                # 2-qadam: Yashirin kod (hashId) topildi! Endi haqiqiy natijalar sahifasiga kiramiz
                details_url = "https://mandat.uzbmb.uz" + link['href']
                details_response = requests.get(details_url, headers=headers)
                
                if details_response.status_code == 200:
                    details_soup = BeautifulSoup(details_response.text, 'html.parser')
                    
                    # Sayt to'liq ochildi! Keyingi qadamda bu yerdan ballarni sug'urib olamiz.
                    # Hozircha muvaffaqiyatli ulanish haqida xabar beramiz.
                    return {
                        "status": "success",
                        "abituriyent_id": abituriyent_id,
                        "qabul_yili": 2026,
                        "xabar": "Yashirin HashId topildi va saytga ulanish muvaffaqiyatli amalga oshdi!",
                        "eslatma": f"Tizim mana bu manzildan ma'lumot o'qidi: {details_url}"
                    }
            else:
                return {"status": "error", "message": f"{abituriyent_id} raqamli ID tizimdan topilmadi yoki kiritishda xato bor."}
                
        else:
            return {"status": "error", "message": f"Test markazi sayti ishlamayapti: {response.status_code}"}
            
    except Exception as e:
        return {"status": "error", "message": f"Dastur xatoligi: {str(e)}"}
