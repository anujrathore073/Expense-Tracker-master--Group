import os

DEBUG = True

# MySQL Configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')  # Default to 'root'
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Kanuka@2211')  # Default to this value
MYSQL_DB = os.environ.get('MYSQL_DB', 'tracker')
MYSQL_CURSORCLASS = 'DictCursor'

# Flask Secret Key
SECRET_KEY = os.environ.get('SECRET_KEY', 'e6456c9ab79838728adf65cd79cd76f1')

