import os

class Config:
    # Usar clave secreta desde variables de entorno, si no existe la crea
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mi_clave_secreta')  
    # Realiza la conexión con la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:1234@localhost:3307/pythonflask')
    # Esta opción hace que continue las modificaciones en la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
