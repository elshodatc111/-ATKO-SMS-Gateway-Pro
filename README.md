# 🚀 ATKO SMS Gateway Pro

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org)

**ATKO SMS Gateway Pro** — bu USB modem orqali O'zbekiston ichidagi telefon raqamlariga avtomatlashtirilgan SMS xabarlarni yuborish uchun professional API yechimi. Statik IP manzilsiz, Cloudflare Tunnel yordamida dunyoning istalgan nuqtasidan lokal modemingizni boshqarish imkonini beradi.



---

## ✨ Asosiy Imkoniyatlar

* **⚡️ Tezkor API:** FastAPI yordamida yozilgan, yuqori tezlikda ishlovchi endpointlar.
* **🌐 Statik IP-siz Ulanish:** Cloudflare Tunnel orqali lokal serverni xavfsiz internetga chiqarish.
* **🛡 Xavfsizlik:** API Token orqali himoyalangan kirish va faqat `+998` (O'zbekiston) raqamlari uchun filtr.
* **📂 Tarixni Saqlash:** Yuborilgan barcha xabarlar SQLite bazasida log ko'rinishida saqlanadi.
* **⚙️ Background Processing:** Modem SMS yuborayotgan vaqtda API kutib turmaydi, darhol javob qaytaradi.

---

## 🛠 Texnologik Stek

* **Backend:** FastAPI (Python)
* **Ma'lumotlar bazasi:** SQLite (SQLAlchemy ORM)
* **Hardware:** GSM/USB Modem (AT-commands)
* **Tunnel:** Cloudflare Tunnel (cloudflared)

---

## ⚙️ O'rnatish va Sozlash

### 1. Loyihani klon qilish
```bash
git clone [https://github.com/username/atko-sms-gateway.git](https://github.com/username/atko-sms-gateway.git)
cd atko-sms-gateway