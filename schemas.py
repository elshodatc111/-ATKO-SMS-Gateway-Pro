from pydantic import BaseModel, validator

class SMSRequest(BaseModel):
    phone: str
    message: str

    @validator('message')
    def message_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Xabar matni bo'sh bo'lishi mumkin emas")
        return v