import os
from dotenv import load_dotenv

load_dotenv()

base_user = os.getenv('BASE_USER')
base_pass = os.getenv('BASE_PASSWORD')
base_name = os.getenv('BASE_NAME')
base_host = os.getenv('BASE_HOST')
base_port = os.getenv('BASE_PORT')

encrytp_salt = b'$2b$08$yINtjjwcwMuOCM6/tHITRO'
jwt_exp_days = 3
secret_key = os.getenv('SECRET_KEY')
algoritm = "HS256"
