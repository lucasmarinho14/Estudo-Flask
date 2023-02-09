import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = 'flash'
import urllib.parse                        
senha = urllib.parse.quote_plus(os.getenv('PASSWORD'))
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = urllib.parse.quote_plus(os.getenv('PASSWORD')),
        servidor = 'localhost',
        database = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'