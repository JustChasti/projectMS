import os
from dotenv import load_dotenv

load_dotenv()

base_user = os.getenv('BASE_USER')
base_pass = os.getenv('BASE_PASSWORD')
base_name = os.getenv('BASE_NAME')
base_host = os.getenv('BASE_HOST')
base_port = os.getenv('BASE_PORT')
