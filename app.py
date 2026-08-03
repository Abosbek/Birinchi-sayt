Enterfrom flask import Flask, jsonify
from mandat_parser import abituriyent_malumotini_olish 

app = Flask(__name__)

# JSON ma'lumotlarda o'zbek kirill/lotin harflari (o', g', q) to'g'ri va chiroyli chiqishi uchun
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    # Asosiy sahifaga kirganda ko'rinadigan matn (HTML formatida)
    return """
    <div style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
        <h1 style="color: #2c3e50;">Abituriyentlar uchun tahlil tizimi (2026) ishlamoqda! 🚀</h1>
        <p style="font-size: 18px; color: #34495e;">
            API ishlashini tekshirish uchun brauzer manzil qatori oxiriga quyidagini qo'shib kiring:
        </p>
        <p style="font-size: 20px; background-color: #ecf0f1; padding: 10px; display: inline-block; border-radius: 5px;">
            <b>/api/check/1234567</b>
        </p>
    </div>
    """

@app.route('/api/check/<int:abituriyent_id>')
def check_id(abituriyent_id):
    # Foydalanuvchi kiritgan ID raqamini parser funksiyasiga beramiz
    natija = abituriyent_malumotini_olish(abituriyent_id)
    
    # Olingan javobni brauzerga JSON (ma'lumot) formatida qaytaramiz
    return jsonify(natija)

if __name__ == '__main__':
    app.run(debug=True)
