# Apna Electrician Image Recognition App

An AI-powered application that recognizes electrical products from images and provides purchase recommendations.

## Features
- Image upload and camera capture
- Product recognition using AI
- WhatsApp notifications
- Email notifications with image attachments
- Purchase recommendations

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

## Configuration
Update the credentials in `config.py` with your own:
- Twilio credentials for WhatsApp
- Email credentials for notifications
- Model URL and paths