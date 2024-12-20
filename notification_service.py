"""Handle all notification services (email and WhatsApp)"""

import os
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config import (
    TWILIO_SID, 
    TWILIO_AUTH_TOKEN,
    SENDER_EMAIL,
    SENDER_PASSWORD,
    RECEIVER_EMAIL
)

class NotificationService:
    def __init__(self):
        self.twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_whatsapp(self, predicted_class, buy_link):
        """Send WhatsApp notification"""
        try:
            self.twilio_client.messages.create(
                from_='whatsapp:+14155238886',
                to='whatsapp:+917800905998',
                body=f"Product detected: {predicted_class}. Buy it here: {buy_link}"
            )
            return True
        except Exception as e:
            print(f"WhatsApp notification failed: {e}")
            return False

    def send_email(self, image_path, predicted_class, buy_link, user_message):
        """Send email notification with image attachment"""
        try:
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = RECEIVER_EMAIL
            msg['Subject'] = "New Product Image Uploaded"
            
            body = f"Detected: {predicted_class}\nBuy here: {buy_link}\nUser Message: {user_message}"
            msg.attach(MIMEText(body, 'plain'))

            with open(image_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(image_path)}'
                )
                msg.attach(part)

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Email notification failed: {e}")
            return False