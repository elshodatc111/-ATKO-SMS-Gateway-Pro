import os
from fastapi import FastAPI, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from models import Base, engine, SessionLocal, SMSLog
from modem_handler import ModemHandler
from schemas import SMSRequest
from utils import verify_token, validate_uz_number

load_dotenv()
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ATKO SMS Gateway Pro")
modem = ModemHandler()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

def process_sms_sending(phone, message, log_id):
    db = SessionLocal()
    success, response = modem.send_sms(phone, message)
    
    log = db.query(SMSLog).filter(SMSLog.id == log_id).first()
    if log:
        log.status = "sent" if success else "failed"
        log.response_msg = response
        db.commit()
    db.close()

@app.post("/send-sms", dependencies=[Depends(verify_token)])
async def send_sms(request: SMSRequest, bg_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # 1. Raqamni tekshirish va filtrdan o'tkazish
    valid_phone = validate_uz_number(request.phone)
    
    # 2. Bazaga "pending" holatida yozish
    new_log = SMSLog(
        phone=valid_phone,
        message=request.message,
        status="pending"
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    
    # 3. Orqa fonda modemga uzatish
    bg_tasks.add_task(process_sms_sending, valid_phone, request.message, new_log.id)
    
    return {
        "status": "accepted", 
        "phone": valid_phone, 
        "log_id": new_log.id
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)