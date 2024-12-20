"""Configuration settings for the application"""

# Twilio credentials
TWILIO_SID = 'AC093d4d6255428d338c2f3edc10328cf7'
TWILIO_AUTH_TOKEN = '40d3d53464a816fb6de7855a640c4194'

# Email credentials
SENDER_EMAIL = "vipulsinghvipul7@gmail.com"
SENDER_PASSWORD = "zazb kspg ecjd brol"
RECEIVER_EMAIL = "vipulsinghvipul7@gmail.com"

# Model settings
MODEL_URL = 'https://github.com/VipulSingh78/vipul/raw/419d4fa1249bd95181d259c202df4e36d873f0c0/Images1/Vipul_Recog_Model.h5'
MODEL_PATH = 'Models/Vipul_Recog_Model.h5'

# Product information
PRODUCT_NAMES = ['Anchor Switch', 'CCTV CAMERA', 'FAN', 'Switch', 'TV']
PRODUCT_LINKS = {
    'Anchor Switch': 'https://www.apnaelectrician.com/anchor-switches',
    'CCTV CAMERA': 'https://www.apnaelectrician.com/cctv-cameras',
    'FAN': 'https://www.apnaelectrician.com/fans',
    'Switch': 'https://www.apnaelectrician.com/switches',
    'TV': 'https://www.apnaelectrician.com/tvs'
}