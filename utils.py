import os
import re
from fastapi import Header, HTTPException
from dotenv import load_dotenv

load_dotenv()

async def verify_token(x_api_token: str = Header(None)):
    if x_api_token != os.getenv("API_ACCESS_TOKEN"):
        raise HTTPException(status_code=403, detail="Ruxsat berilmagan token!")
    return x_api_token

def validate_uz_number(phone: str) -> str:
    # Bo'shliqlarni va ortiqcha belgilarni olib tashlaymiz
    clean_phone = re.sub(r'[\s\-\(\)]', '', phone)
    
    # Agar raqam 998 bilan boshlanmasa, uni qo'shamiz (masalan: 901234567 -> +998901234567)
    if clean_phone.startswith('9') and len(clean_phone) == 9:
        clean_phone = '+998' + clean_phone
    elif clean_phone.startswith('8'): # 890... bo'lsa
        clean_phone = '+998' + clean_phone[1:]
    
    # O'zbekiston raqami formati: +998XXXXXXXXX (13 ta belgi)
    pattern = r'^\+998\d{9}$'
    if not re.match(pattern, clean_phone):
        raise HTTPException(status_code=400, detail="Faqat O'zbekiston raqamlariga SMS yuborish mumkin! (+998...)")
    
    return clean_phone