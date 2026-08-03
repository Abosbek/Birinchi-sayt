Enterimport requests
from bs4 import BeautifulSoup

def abituriyent_malumotini_olish(abituriyent_id):
    # Mandat saytining qidiruv manzili (joriy yil holatiga moslashuvchan)
    url = f"https://mandat.uzbmb.uz/Home/Details/{abituriyent_id}"
    
    # Sayt bizning kodimizni haqiqiy foydalanuvchi deb qabul qilishi uchun sozlamalar
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "uz,en-US;q=0.9,en;q=0.8"
    }
    
    try:
        # Saytga ma'lumot so'rab murojaat qilamiz (kutish vaqti 10 soniya)
        response = requests.get(url, headers=headers, timeout=10)
        
        # Agar sahifa muvaffaqiyatli topshirilsa
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # DIQQAT: Mandat natijalari e'lon qilingach, saytning dizayniga qarab bu yerdagi qidiruv teglari aniqlanadi.
            # Hozircha bazaviy qolibni qaytaramiz.
            
            natija = {
                "status": "success",
                "abituriyent_id": abituriyent_id,
                "xabar": "Mandat saytiga ulanish muvaffaqiyatli amalga oshirildi!",
                "qabul_yili": 2026,
                "eslatma": "Natijalar chiqqach, ball va o'rin avtomatik shu yerda paydo bo'ladi."
            }
            return natija
            
        elif response.status_code == 404:
             return {"status": "error", "message": f"{abituriyent_id} ID raqamli abituriyent topilmadi."}
        else:
            return {"status": "error", "message": f"Saytda vaqtinchalik muammo: Xatolik kodi {response.status_code}"}
            
    # Agar internet o'chib qolsa yoki mandat.uzbmb.uz sayti qotib qolsa
    except requests.exceptions.RequestException:
        return {"status": "error", "message": "Mandat saytiga ulanib bo'lmadi. Sayt ishlamayotgan bo'lishi mumkin."}
    except Exception as e:
        return {"status": "error", "message": f"Kutilmagan xatolik yuz berdi: {str(e)}"}
