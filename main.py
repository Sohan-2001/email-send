import os
import smtplib
from email.message import EmailMessage
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

app = FastAPI()

class EmailRequest(BaseModel):
    host: str  # SMTP server host, e.g., 'smtp.gmail.com'
    to: str
    subject: str
    body: str

@app.post("/send-email")
def send_email(request: EmailRequest):
    msg = EmailMessage()
    msg["Subject"] = request.subject+ " - Sohan Karfa does not take responsibility for any issues caused by this email."
    msg["From"] = EMAIL_SENDER
    msg["To"] = request.to
    msg.set_content(request.body)

    try:
        with smtplib.SMTP(request.host, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
