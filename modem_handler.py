import serial
import time
import os
from dotenv import load_dotenv

load_dotenv()

class ModemHandler:
    def __init__(self):
        self.port = os.getenv("MODEM_PORT")
        self.baud = int(os.getenv("MODEM_BAUD_RATE", 115200))
        self.timeout = int(os.getenv("MODEM_TIMEOUT", 5))

    def send_sms(self, phone: str, message: str):
        ser = None
        try:
            ser = serial.Serial(self.port, self.baud, timeout=self.timeout)
            
            # 1. Modemni uyg'otish va Text mode
            ser.write(b'AT\r')
            time.sleep(0.5)
            ser.write(b'AT+CMGF=1\r') 
            time.sleep(0.5)
            
            # 2. Raqam va Matn yuborish
            ser.write(f'AT+CMGS="{phone}"\r'.encode())
            time.sleep(0.5)
            ser.write(message.encode() + b"\x1a")
            
            # 3. Natijani kutish (maksimum 5 soniya)
            time.sleep(5)
            response = ser.read_all().decode(errors='ignore')
            ser.close()

            if "OK" in response and "+CMGS" in response:
                return True, response
            return False, response
        except Exception as e:
            if ser and ser.is_open: ser.close()
            return False, str(e)

    # Modem qotib qolsa yoki har 100 ta SMSdan keyin ishlatish uchun
    def reboot_modem(self):
        try:
            ser = serial.Serial(self.port, self.baud, timeout=self.timeout)
            ser.write(b'AT+CFUN=1,1\r') # Modemni dasturiy qayta yuklash
            ser.close()
            return True
        except:
            return False