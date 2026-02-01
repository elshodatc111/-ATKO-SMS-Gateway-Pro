from sqlalchemy import Column, Integer, String, DateTime, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os
from dotenv import load_dotenv

# .env faylidagi DATABASE_URL ni yuklaymiz
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")

# Bazaning asosi
Base = declarative_base()

class SMSLog(Base):
    """
    Yuborilgan har bir SMS ma'lumotlarini saqlash uchun jadval
    """
    __tablename__ = "sms_logs"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(20), nullable=False)      # Qabul qiluvchi raqami
    message = Column(Text, nullable=False)         # SMS matni
    status = Column(String(20))                    # 'sent' (yuborildi) yoki 'failed' (xato)
    response_msg = Column(String(255))             # Modemdan kelgan texnik javob
    created_at = Column(DateTime, default=datetime.datetime.utcnow) # Vaqti

# Bazaga ulanishni sozlash
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)